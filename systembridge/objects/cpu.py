"""
Class object for Cpu
Documentation: https://system-bridge.timmo.dev
"""
from .base import BridgeBase


class Cache(BridgeBase):
    @property
    def l1d(self):
        return self.attributes.get("l1d", None)

    @property
    def l1i(self):
        return self.attributes.get("l1i", None)

    @property
    def l2(self):
        return self.attributes.get("l2", None)

    @property
    def l3(self):
        return self.attributes.get("l3", None)


class CpuCache(BridgeBase):
    @property
    def l1d(self):
        return self.attributes.get("l1d", None)

    @property
    def l1i(self):
        return self.attributes.get("l1i", None)

    @property
    def l2(self):
        return self.attributes.get("l2", None)

    @property
    def l3(self):
        return self.attributes.get("l3", None)


class CpuInner(BridgeBase):
    @property
    def manufacturer(self):
        return self.attributes.get("manufacturer", "")

    @property
    def brand(self):
        return self.attributes.get("brand", "")

    @property
    def vendor(self):
        return self.attributes.get("vendor", "")

    @property
    def family(self):
        return self.attributes.get("family", "")

    @property
    def model(self):
        return self.attributes.get("model", "")

    @property
    def stepping(self):
        return self.attributes.get("stepping", "")

    @property
    def revision(self):
        return self.attributes.get("revision", "")

    @property
    def voltage(self):
        return self.attributes.get("voltage", "")

    @property
    def speed(self):
        return self.attributes.get("speed", None)

    @property
    def speedMin(self):
        return self.attributes.get("speedMin", None)

    @property
    def speedMax(self):
        return self.attributes.get("speedMax", None)

    @property
    def governor(self):
        return self.attributes.get("governor", "")

    @property
    def cores(self):
        return self.attributes.get("cores", None)

    @property
    def physicalCores(self):
        return self.attributes.get("physicalCores", None)

    @property
    def processors(self):
        return self.attributes.get("processors", None)

    @property
    def socket(self):
        return self.attributes.get("socket", "")

    @property
    def flags(self):
        return self.attributes.get("flags", "")

    @property
    def virtualization(self):
        return self.attributes.get("virtualization", False)

    @property
    def cache(self):
        return CpuCache(self.attributes.get("cache", {}))


class CurrentSpeed(BridgeBase):
    @property
    def min(self):
        return self.attributes.get("min", None)

    @property
    def max(self):
        return self.attributes.get("max", None)

    @property
    def avg(self):
        return self.attributes.get("avg", None)

    @property
    def cores(self):
        return self.attributes.get("cores", None)


class Temperature(BridgeBase):
    @property
    def main(self):
        return self.attributes.get("main", None)

    @property
    def max(self):
        return self.attributes.get("max", None)


class Cpu(BridgeBase):
    @property
    def cache(self):
        return Cache(self.attributes.get("cache", {}))

    @property
    def cpu(self):
        return CpuInner(self.attributes.get("cpu", {}))

    @property
    def currentSpeed(self):
        return CurrentSpeed(self.attributes.get("currentSpeed", {}))

    @property
    def temperature(self):
        return Temperature(self.attributes.get("temperature", {}))
