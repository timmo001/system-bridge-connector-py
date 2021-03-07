"""
Class object for CommandPayload
Documentation: https://system-bridge.timmo.dev

Generated by generator/generator.py - 2021-02-20 16:53:35.135485
"""
from ..base import BridgeBase


class CommandPayload(BridgeBase):
    @property
    def command(self):
        return self.attributes.get("command", "")

    @property
    def arguments(self):
        return self.attributes.get("arguments", [])

    @property
    def wait(self):
        return self.attributes.get("wait", True)
