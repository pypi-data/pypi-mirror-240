from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
from pylibrm.constant import const
import time
from enum import Enum

class Axis_V6(object):
    def __init__(self, client: ModbusClient, slave_id: int):
        self._slave_id = slave_id
        self._client = client
        self._io_gap_time = 10  # ms
        self._retries = 0
        self._is_debug = False
        pass

    def _print(self, v):
        if self._is_debug:
            print(v)

    def wait(self, time_in_ms):
        time.sleep(time_in_ms / 1000.0)

    def wait_for_reached(self, timeout):
        timeout = timeout/1000.
        start_time = time.time()
        while True:
            last_time = time.time() - start_time
            if last_time > timeout:
                break
            is_reached = self.is_reached()
            if is_reached:
                break
        pass

    def retry(self, func):
        def wrapper(*args, **kwargs):
            count = 0
            while True:
                r = func(*args, **kwargs)

                if count > self._retries:
                    break

                if not r.isError():
                    break
                else:
                    self._print(r)
                count += 1
                self._print("axis" + str(self._slave_id) + " retry " + str(func) + str(args))
            return r

        return wrapper

    @staticmethod
    def create_modbus_rtu(port, slave_id, baudrate=115200):
        client = ModbusClient(method="rtu", port=port, stopbits=1, timeout=0.01,
                              bytesize=8, parity='N', baudrate=baudrate, retries=10, strict=False)
        connection = client.connect()
        return Axis_V6(client, slave_id)

    def read_int32(self, address, func):
        r = self.retry(func)(address, 2, unit=self._slave_id)
        return BinaryPayloadDecoder.fromRegisters(r.registers, wordorder=Endian.Little, byteorder=Endian.Big)

    def read_float(self, address, func):
        r = self.retry(func)(address, 2, unit=self._slave_id)
        decoder = BinaryPayloadDecoder.fromRegisters(r.registers, wordorder=Endian.Little, byteorder=Endian.Big)
        return decoder.decode_32bit_float()

    def read_input_int32(self, address):
        return self.read_int32(address, self._client.read_input_registers).decode_32bit_int()

    def read_input_float(self, address):
        return self.read_float(address, self._client.read_input_registers)

    def read_holding_int32(self, address):
        return self.read_int32(address, self._client.read_holding_registers).decode_32bit_int()

    def read_holding_float(self, address):
        return self.read_float(address, self._client.read_holding_registers)

    def write_regs(self, address, data):
        return self._client.write_registers(address, data, skip_encode=True, unit=self._slave_id)

    def write_int32(self, address, value):
        builder = BinaryPayloadBuilder(wordorder=Endian.Little, byteorder=Endian.Big)
        builder.add_32bit_int(int(value))
        return self.write_regs(address, builder.build())

    def write_float(self, address, value):
        builder = BinaryPayloadBuilder(wordorder=Endian.Little, byteorder=Endian.Big)
        builder.add_32bit_float(int(value))
        return self.write_regs(address, builder.build())
    

    def write_holding_float(self, address, value):
        self.write_float(address, value)

    def write_holding_int32(self, address, value):
        self.write_int32(address, value)

    def write_coil(self, address, value):
        self._client.write_coil(address, value, unit=self._slave_id)

    def trig_coil(self, address):
        self.write_coil(address, False)
        self.wait(self._io_gap_time)
        self.write_coil(address, True)

    def read_coil(self, address):
        r = self._client.read_coils(address, unit=self._slave_id)
        return r.bits[0]

    def get_version(self):
        version = dict()
        version["major"] = self.read_input_int32(8)
        version["minor"] = self.read_input_int32(10)
        version["build"] = self.read_input_int32(12)
        version["type"] = self.read_input_int32(14)
        return version

    def config_motion(self, velocity, acceleration):
        self.write_holding_float(2286, velocity)
        self.write_holding_float(2288, acceleration)

    def read_config_motion(self):
        return [self.read_holding_float(2286), self.read_holding_float(2288)]

    def move_to(self, position):
        self.write_holding_float(2284, position)

    def set_command(self, index, command):
        builder = BinaryPayloadBuilder(wordorder=Endian.Little, byteorder=Endian.Big)
        builder.add_32bit_int(int(command["type"]))
        builder.add_32bit_int(int(command["next_command_index"]))
        
        if command["type"] ==  const.COMMAND_GO_HOME:
            builder.add_32bit_float(float(command["origin_offset"]))
        elif command["type"] ==  const.COMMAND_DELAY:
            builder.add_32bit_int(int(command["ms"]))
        elif command["type"] ==  const.COMMAND_MOVE_ABSOLUTE:
            builder.add_32bit_float(float(command["position"]))
            builder.add_32bit_float(float(command["velocity"]))
            builder.add_32bit_float(float(command["acceleration"]))
            builder.add_32bit_float(float(command["deceleration"]))
            builder.add_32bit_float(float(command["band"]))
        elif command["type"] ==  const.COMMAND_MOVE_RELATIVE:
            builder.add_32bit_float(float(command["distance"]))
            builder.add_32bit_float(float(command["velocity"]))
            builder.add_32bit_float(float(command["acceleration"]))
            builder.add_32bit_float(float(command["deceleration"]))
            builder.add_32bit_float(float(command["band"]))
        elif command["type"] == const.COMMAND_PUSH:
            builder.add_32bit_float(float(command["distance"]))
            builder.add_32bit_float(float(command["velocity"]))
            builder.add_32bit_float(float(command["acceleration"]))
            builder.add_32bit_float(float(command["force_limit"]))
            builder.add_32bit_float(float(command["band_mm"]))
            builder.add_32bit_float(float(command["time_band_ms"]))
        elif command["type"] ==  const.COMMAND_PRECISE_PUSH:
            builder.add_32bit_float(float(command["distance"]))
            builder.add_32bit_float(float(command["force"]))
            builder.add_32bit_float(float(command["velocity_factor"]))
            builder.add_32bit_float(float(command["impact_factor"]))
            builder.add_32bit_float(float(command["band_n"]))
            builder.add_32bit_float(float(command["band_ms"]))
        elif command["type"] ==  const.COMMAND_GO_HOME_Z:
            builder.add_32bit_float(float(command["distance"]))
            builder.add_32bit_float(float(command["velocity"]))
            builder.add_32bit_float(float(command["acceleration"]))
            builder.add_32bit_float(float(command["force_limit"]))
            builder.add_32bit_float(float(command["band_mm"]))
        elif command["type"] ==  const.COMMAND_PRECISE_TOUCH:
            builder.add_32bit_float(float(command["distance"]))
            builder.add_32bit_float(float(command["velocity"]))
            builder.add_32bit_float(float(command["acceleration"]))
            builder.add_32bit_float(float(command["force_threshold"]))
            builder.add_32bit_float(float(command["band_mm"]))
        elif command["type"] == const.COMMAND_START_MONITOR:
            builder.add_32bit_int(int(command["freq_hz"]))
            builder.add_32bit_int(int(command["length"]))
            builder.add_32bit_int(int(command["count"]))
            builder.add_32bit_int(int(command["var_0"]))
            builder.add_32bit_int(int(command["var_1"]))
            builder.add_32bit_int(int(command["var_2"]))
        return self.write_regs(5000 + index * 16, builder.build())


    def trig_command(self, index):
        self.write_holding_int32(2000, index)
        self.trig_coil(2)

    def exec_command(self, command):
        self.set_command(32, command)
        self.trig_command(32)

    def precise_push(self, distance, force, velocity_factor, impact_factor, band_n, band_ms):
        command = dict()
        command["type"] = const.COMMAND_PRECISE_PUSH
        command["next_command_index"] = -1
        command["distance"] = distance
        command["force"] = force
        command["velocity_factor"] = velocity_factor
        command["impact_factor"] = impact_factor
        command["band_n"] = band_n
        command["band_ms"] = band_ms
        self.exec_command(command)
        
    def move_absolute(self, position, velocity, acceleration, deceleration, band):
        command = dict()
        command["type"] = 3
        command["next_command_index"] = -1
        command["position"] = position
        command["velocity"] = velocity
        command["acceleration"] = acceleration
        command["deceleration"] = deceleration
        command["band"] = band
        self.exec_command(command)
        

    def go_home(self):
        self.trig_coil(17)


    def is_moving(self):
        if self.read_coil(1015):
            return False
        if  self.read_input_float(2) > 2 or self.read_input_float(2) < -2:
            return True
        else:
            return False

    def is_push_empty(self):
        if self.read_input_float(18) == 3:
            return True
        else:
            return False

    def error_code(self):
        ret = 0
        if self.read_coil(2020):
            ret -= 10
        if self.read_coil(2018):
            ret -= 20
        if self.read_coil(3):
            ret -= 40

    def reset_error(self):
        self.write_coil(0, 0)
        self.write_coil(0, 1)

    def reset_force(self):
        self.write_coil(16, 0)
        self.write_coil(16, 1)

    def set_servo_on_off(self, on_off):
        self.write_coil(1, on_off)

    def stop(self):
        self.trig_coil(3)

    def position(self):
        return self.read_input_float(0)

    def force_sensor(self):
        return self.read_input_float(16)

    def close(self):
        self._client.close()


class Axis_V4(object):
    def __init__(self, client: ModbusClient, slave_id: int):
        self._slave_id = slave_id
        self._client = client
        self._io_gap_time = 10  # ms
        self._retries = 0
        self._is_debug = False
        pass

    def _print(self, v):
        if self._is_debug:
            print(v)

    def wait(self, time_in_ms):
        time.sleep(time_in_ms / 1000.0)

    def wait_for_reached(self, timeout):
        timeout = timeout/1000.
        start_time = time.time()
        while True:
            last_time = time.time() - start_time
            if last_time > timeout:
                break
            is_reached = self.is_reached()
            if is_reached:
                break
        pass

    def retry(self, func):
        def wrapper(*args, **kwargs):
            count = 0
            while True:
                r = func(*args, **kwargs)

                if count > self._retries:
                    break

                if not r.isError():
                    break
                else:
                    self._print(r)
                count += 1
                self._print("axis" + str(self._slave_id) + " retry " + str(func) + str(args))
            return r

        return wrapper

    @staticmethod
    def create_modbus_rtu(port, slave_id, baudrate=115200):
        client = ModbusClient(method="rtu", port=port, stopbits=1, timeout=0.01,
                              bytesize=8, parity='N', baudrate=baudrate, retries=10, strict=False)
        connection = client.connect()
        return Axis_V4(client, slave_id)

    def read_int32(self, address, func):
        r = self.retry(func)(address, 2, unit=self._slave_id)
        return BinaryPayloadDecoder.fromRegisters(r.registers, wordorder=Endian.Big, byteorder=Endian.Big)

    def read_input_int32(self, address):
        return self.read_int32(address, self._client.read_input_registers).decode_32bit_int()

    def read_input_float(self, address):
        return self.read_int32(address, self._client.read_input_registers).decode_32bit_int() / 1000.0

    def read_holding_int32(self, address):
        return self.read_int32(address, self._client.read_holding_registers).decode_32bit_int()

    def read_holding_float(self, address):
        return self.read_int32(address, self._client.read_holding_registers).decode_32bit_int() / 1000.0

    def write_regs(self, address, data):
        return self._client.write_registers(address, data, skip_encode=True, unit=self._slave_id)

    def write_int32(self, address, value):
        builder = BinaryPayloadBuilder(wordorder=Endian.Big, byteorder=Endian.Big)
        builder.add_32bit_int(int(value))
        return self.write_regs(address, builder.build())

    def write_holding_float(self, address, value):
        self.write_int32(address, value * 1000.0)

    def write_holding_int32(self, address, value):
        self.write_int32(address, value)

    def write_coil(self, address, value):
        self._client.write_coil(address, value, unit=self._slave_id)

    def trig_coil(self, address):
        self.write_coil(address, False)
        self.wait(self._io_gap_time)
        self.write_coil(address, True)

    def read_coil(self, address):
        r = self._client.read_coils(address, unit=self._slave_id)
        return r.bits[0]

    def get_version(self):
        version = dict()
        version["major"] = self.read_input_int32(8)
        version["minor"] = self.read_input_int32(10)
        version["build"] = self.read_input_int32(12)
        version["type"] = self.read_input_int32(14)
        return version

    def config_motion(self, velocity, acceleration, deceleration):
        self.write_holding_float(4904, velocity)
        self.write_holding_float(4906, acceleration)
        self.write_holding_float(4908, deceleration)

    def read_config_motion(self):
        return [self.read_holding_float(4902), self.read_holding_float(4904), self.read_holding_float(4906)]

    def move_to(self, position):
        self.write_holding_float(4902, position)

    def set_command(self, index, command):
        builder = BinaryPayloadBuilder(wordorder=Endian.Big, byteorder=Endian.Big)
        builder.add_32bit_int(int(command["type"]))
        builder.add_32bit_int(int(command["position"] * 1000))
        builder.add_32bit_int(int(command["velocity"] * 1000))
        builder.add_32bit_int(int(command["acceleration"] * 1000))
        builder.add_32bit_int(int(command["deceleration"] * 1000))
        builder.add_32bit_int(int(command["band"] * 1000))
        builder.add_32bit_int(int(command["push_force"] * 1000))
        builder.add_32bit_int(int(command["push_distance"] * 1000))
        builder.add_32bit_int(int(command["delay"]))
        builder.add_32bit_int(int(command["next_command_index"]))
        return self.write_regs(5000 + index * 20, builder.build())

    def trig_command(self, index):
        self.write_holding_int32(4001, index)
        self.trig_coil(const.IO_IN_START)

    def exec_command(self, command):
        self.set_command(const.EXECUTE_COMMAND_INDEX, command)
        self.trig_command(const.EXECUTE_COMMAND_INDEX)

    def precise_push(self, force, distance, velocity, force_band, force_check_time):
        command = dict()
        command["type"] = const.COMMAND_CLOSED_LOOP_PUSH
        command["position"] = 0
        command["velocity"] = velocity
        command["acceleration"] = 0
        command["deceleration"] = 0
        command["band"] = force_band
        command["push_force"] = force / self.get_force_scale()
        command["push_distance"] = distance
        command["delay"] = force_check_time
        command["next_command_index"] = -1
        self.exec_command(command)

    def move_absolute(self, position, velocity, acceleration, deceleration, band):
        command = dict()
        command["type"] = const.COMMAND_MOVE_ABSOLUTE
        command["position"] = position
        command["velocity"] = velocity
        command["acceleration"] = acceleration
        command["deceleration"] = deceleration
        command["band"] = band
        command["push_force"] = 0
        command["push_distance"] = 0
        command["delay"] = 0
        command["next_command_index"] = -1
        self.exec_command(command)

    def go_home(self):
        self.trig_coil(const.IO_IN_GO_HOME)

    def is_moving(self):
        return self.read_coil(1505)

    def is_reached(self):
        return self.read_coil(1521)

    def is_push_empty(self):
        return ~self.is_moving()

    def error_code(self):
        return self.read_input_int32(6)

    def reset_error(self):
        self.write_coil(const.IO_IN_ERROR_RESET, 0)
        self.write_coil(const.IO_IN_ERROR_RESET, 1)

    def reset_force(self):
        self.write_coil(const.IO_IN_FORCE_RESET, 0)
        self.write_coil(const.IO_IN_FORCE_RESET, 1)

    def set_servo_on_off(self, on_off):
        self.write_coil(const.IO_IN_SERVO, on_off)

    def stop(self):
        self.trig_coil(const.IO_IN_STOP)

    def position(self):
        return self.read_input_float(0)

    def force_sensor(self):
        return self.read_input_float(18) * self.get_force_scale()

    def set_force_scale(self,force_factor):
        self.write_holding_int32(5000+20*32, int(force_factor * 1000.0))

    def get_force_scale(self):
        return self.read_holding_int32(5000+20*32) / 1000.0

    def close(self):
        self._client.close()

class Axis(Axis_V4):
    pass
