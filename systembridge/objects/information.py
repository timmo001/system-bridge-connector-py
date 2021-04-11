"""
Class object for Information
Documentation: https://system-bridge.timmo.dev
"""
from .base import BridgeBase


class Endpoint(BridgeBase):
    @property
    def description(self):
        return self.attributes.get("description", "")

    @property
    def endpoint(self):
        return self.attributes.get("endpoint", "")


class Information(BridgeBase):
    @property
    def audio(self):
        return Endpoint(self.attributes.get("audio", {}))

    @property
    def battery(self):
        return Endpoint(self.attributes.get("battery", {}))

    @property
    def bluetooth(self):
        return Endpoint(self.attributes.get("bluetooth", {}))

    @property
    def command(self):
        return Endpoint(self.attributes.get("command", {}))

    @property
    def cpu(self):
        return Endpoint(self.attributes.get("cpu", {}))

    @property
    def docs(self):
        return Endpoint(self.attributes.get("docs", {}))

    @property
    def filesystem(self):
        return Endpoint(self.attributes.get("filesystem", {}))

    @property
    def graphics(self):
        return Endpoint(self.attributes.get("graphics", {}))

    @property
    def information(self):
        return Endpoint(self.attributes.get("information", {}))

    @property
    def memory(self):
        return Endpoint(self.attributes.get("memory", {}))

    @property
    def network(self):
        return Endpoint(self.attributes.get("network", {}))

    @property
    def os(self):
        return Endpoint(self.attributes.get("os", {}))

    @property
    def system(self):
        return Endpoint(self.attributes.get("system", {}))
