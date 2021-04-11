"""
Class object for Battery
Documentation: https://system-bridge.timmo.dev
"""
from .base import BridgeBase


class Battery(BridgeBase):
    @property
    def hasBattery(self):
        return self.attributes.get("hasBattery", False)

    @property
    def cycleCount(self):
        return self.attributes.get("cycleCount", None)

    @property
    def isCharging(self):
        return self.attributes.get("isCharging", False)

    @property
    def designedCapacity(self):
        return self.attributes.get("designedCapacity", None)

    @property
    def maxCapacity(self):
        return self.attributes.get("maxCapacity", None)

    @property
    def currentCapacity(self):
        return self.attributes.get("currentCapacity", None)

    @property
    def voltage(self):
        return self.attributes.get("voltage", None)

    @property
    def capacityUnit(self):
        return self.attributes.get("capacityUnit", "")

    @property
    def percent(self):
        return self.attributes.get("percent", None)

    @property
    def timeRemaining(self):
        return self.attributes.get("timeRemaining", None)

    @property
    def acConnected(self):
        return self.attributes.get("acConnected", True)

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def model(self):
        return self.attributes.get("model", "")

    @property
    def manufacturer(self):
        return self.attributes.get("manufacturer", "")

    @property
    def serial(self):
        return self.attributes.get("serial", "")
