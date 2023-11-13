import logging
from typing import List
from ppadb.client import Client
from ppadb.device import Device

log = logging.getLogger(__name__)


class DefaultCpuTempSampler:
    TEMP_FILE_PATHS = [
        "/sys/devices/system/cpu/cpu0/cpufreq/cpu_temp",
        "/sys/devices/system/cpu/cpu0/cpufreq/FakeShmoo_cpu_temp",
        "/sys/class/thermal/thermal_zone0/temp",
        "/sys/class/i2c-adapter/i2c-4/4-004c/temperature",
        "/sys/devices/platform/tegra-i2c.3/i2c-4/4-004c/temperature",
        "/sys/devices/platform/omap/omap_temp_sensor.0/temperature",
        "/sys/devices/platform/tegra_tmon/temp1_input",
        "/sys/kernel/debug/tegra_thermal/temp_tj",
        "/sys/devices/platform/s5p-tmu/temperature",
        "/sys/class/thermal/thermal_zone1/temp",
        "/sys/class/hwmon/hwmon0/device/temp1_input",
        "/sys/devices/virtual/thermal/thermal_zone1/temp",
        "/sys/devices/virtual/thermal/thermal_zone0/temp",
        "/sys/class/thermal/thermal_zone3/temp",
        "/sys/class/thermal/thermal_zone4/temp",
        "/sys/class/hwmon/hwmonX/temp1_input",
        "/sys/devices/platform/s5p-tmu/curr_temp",
    ]

    def __init__(self, device: Device) -> None:
        self.device = device
        self.cpu_temp_valid_path = None

    def cpu_temp(self):
        if not self.cpu_temp_valid_path:
            for path in self.TEMP_FILE_PATHS:
                temp = self.__try_get_temp(path)
                if temp is None:
                    continue
                else:
                    return temp
        else:
            return self.__try_get_temp(self.cpu_temp_valid_path)

    def __try_get_temp(self, path):
        try:
            print(f"读取 {path}")
            result = self.device.shell(f"cat {path}")
            temp = float(result)
            print(f"{temp} valid {self.is_temp_valid(temp)}")
            print(f"{temp/1000} valid {self.is_temp_valid(temp/1000)}")
            if self.is_temp_valid(temp):
                self.cpu_temp_valid_path = path
                return temp
            elif self.is_temp_valid(temp / 1000):
                self.cpu_temp_valid_path = path
                return temp / 1000
        except Exception as e:
            print(e)
            return None

    def is_temp_valid(self, value):
        return -30 <= value <= 250


class MarkTempSampler:
    CPU_MARKS = [
        "mtktscpu",  # 联发科
        "tsens_tz_sensor",  # 高通
        "exynos",  # 三星
        "sdm-therm",  # 高通晓龙
        "cpu-0-0-us",  # 通用
        "soc_thermal",  # 通用
        "cpu",  # 通用
    ]
    BATTERY_MARKS = ["battery", "Battery"]
    NPU_MARKS = ["npu-usr", "npu"]
    GPU_MARKS = ["gpuss-0-us", "gpu"]

    SENSOR_LIST_CMD = "cat /sys/devices/virtual/thermal/thermal_zone*/type"
    SENSOR_FILE_LIST_CMD = "cd /sys/devices/virtual/thermal/ && ls|grep thermal_zone"
    SENSOR_TEMP_LIST_CMD = "cat /sys/devices/virtual/thermal/thermal_zone*/temp"
    TEMP_CMD = "cat /sys/devices/virtual/thermal/{filename}/temp"

    def __init__(self, device: Device) -> None:
        self.device = device
        self._sensor_list = self.get_sensor_list()
        self._sensor_filename_list = self.get_sensor_filename_list()
        self.prop = self.device.get_properties()

    def get_sensor_list(self):
        list_str: str = self.device.shell(self.SENSOR_LIST_CMD)
        return list_str.split("\n")

    def get_sensor_filename_list(self):
        list_str: str = self.device.shell(self.SENSOR_FILE_LIST_CMD)
        return list_str.split("\n")

    def get_sensor_temp(self, index: int):
        file_name = self._sensor_filename_list[index]
        temp_value = self.device.shell(self.TEMP_CMD.format(filename=file_name)) or "0"
        temp_value = self.str_to_temp(temp_value)

        return temp_value

    def get_senser_index(self, marks):
        sensor_list: List[str] = self._sensor_list
        for mark in marks:
            for index, sensor_name in enumerate(sensor_list):
                if sensor_name.lower().startswith(mark):
                    return index

        manufacturer = self.prop["ro.product.manufacturer"]  # 制造商
        model = self.prop["ro.product.model"]  # 型号
        log.warning(f"{manufacturer}-{model} 没有匹配到{marks} 无法获得其温度，改用整体温度表示")
        return 0

    def is_temp_valid(self, value):
        return -30 <= value <= 250

    def get_temp(self):
        total_temp_index = 0
        cpu_temp_index = self.get_senser_index(self.CPU_MARKS)
        gpu_temp_index = self.get_senser_index(self.GPU_MARKS)
        npu_temp_index = self.get_senser_index(self.NPU_MARKS)
        battery_temp_index = self.get_senser_index(self.BATTERY_MARKS)

        total_temp = (
            self.get_sensor_temp(total_temp_index)
            if total_temp_index is not None
            else 0
        )
        cpu_temp = (
            self.get_sensor_temp(cpu_temp_index) if cpu_temp_index is not None else 0
        )
        gpu_temp = (
            self.get_sensor_temp(gpu_temp_index) if gpu_temp_index is not None else 0
        )
        npu_temp = (
            self.get_sensor_temp(npu_temp_index) if npu_temp_index is not None else 0
        )
        battery_temp = (
            self.get_sensor_temp(battery_temp_index)
            if battery_temp_index is not None
            else 0
        )

        return {
            "total": total_temp,
            "cpu": cpu_temp,
            "gpu": gpu_temp,
            "npu": npu_temp,
            "battery": battery_temp,
        }

    def str_to_temp(self, txt: str):
        try:
            temp = float(txt)
            if self.is_temp_valid(temp):
                return temp
            elif self.is_temp_valid(temp / 10):
                return temp / 10
            elif self.is_temp_valid(temp / 1000):
                return temp / 1000
            return 0
        except Exception:
            return -1


if __name__ == "__main__":
    from ppadb.client import Client

    adb = Client()
    dev = adb.devices()[0]

    util = MarkTempSampler(dev)
    print(util.get_senser_index(util.CPU_MARKS))
    print("all", util.get_temp())
