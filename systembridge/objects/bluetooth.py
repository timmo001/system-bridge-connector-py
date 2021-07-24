"""
Class object for BridgeBluetooth
Documentation: https://system-bridge.timmo.dev
"""
from .base import BridgeBase


class Bluetooth(BridgeBase):
    @property
    def device(self):
        return self.attributes.get("device", "")

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def manufacturer(self):
        return self.attributes.get("manufacturer", "")

    @property
    def macDevice(self):
        return self.attributes.get("macDevice", "")

    @property
    def macHost(self):
        return self.attributes.get("macHost", "")

    @property
    def batteryPercent(self):
        return self.attributes.get("batteryPercent", "")

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def connected(self):
        return self.attributes.get("connected", "")
