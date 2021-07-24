"""
Class object for System
Documentation: https://system-bridge.timmo.dev
"""
from .base import BridgeBase


class Baseboard(BridgeBase):
    @property
    def manufacturer(self):
        return self.attributes.get("manufacturer", "")

    @property
    def model(self):
        return self.attributes.get("model", "")

    @property
    def version(self):
        return self.attributes.get("version", "")

    @property
    def serial(self):
        return self.attributes.get("serial", "")

    @property
    def assetTag(self):
        return self.attributes.get("assetTag", "")

    @property
    def memMax(self):
        return self.attributes.get("memMax", None)

    @property
    def memSlots(self):
        return self.attributes.get("memSlots", None)


class Bios(BridgeBase):
    @property
    def vendor(self):
        return self.attributes.get("vendor", "")

    @property
    def version(self):
        return self.attributes.get("version", "")

    @property
    def releaseDate(self):
        return self.attributes.get("releaseDate", "")

    @property
    def revision(self):
        return self.attributes.get("revision", "")


class Chassis(BridgeBase):
    @property
    def manufacturer(self):
        return self.attributes.get("manufacturer", "")

    @property
    def model(self):
        return self.attributes.get("model", "")

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def version(self):
        return self.attributes.get("version", "")

    @property
    def serial(self):
        return self.attributes.get("serial", "")

    @property
    def assetTag(self):
        return self.attributes.get("assetTag", "")

    @property
    def sku(self):
        return self.attributes.get("sku", "")


class SystemInner(BridgeBase):
    @property
    def manufacturer(self):
        return self.attributes.get("manufacturer", "")

    @property
    def model(self):
        return self.attributes.get("model", "")

    @property
    def version(self):
        return self.attributes.get("version", "")

    @property
    def serial(self):
        return self.attributes.get("serial", "")

    @property
    def uuid(self):
        return self.attributes.get("uuid", "")

    @property
    def sku(self):
        return self.attributes.get("sku", "")

    @property
    def virtual(self):
        return self.attributes.get("virtual", False)


class Uuid(BridgeBase):
    @property
    def os(self):
        return self.attributes.get("os", "")

    @property
    def hardware(self):
        return self.attributes.get("hardware", "")

    @property
    def macs(self):
        return self.attributes.get("macs", [])


class System(BridgeBase):
    @property
    def baseboard(self):
        return Baseboard(self.attributes.get("baseboard", {}))

    @property
    def bios(self):
        return Bios(self.attributes.get("bios", {}))

    @property
    def chassis(self):
        return Chassis(self.attributes.get("chassis", {}))

    @property
    def system(self):
        return SystemInner(self.attributes.get("system", {}))

    @property
    def uuid(self):
        return Uuid(self.attributes.get("uuid", {}))
