"""
Class object for CommandResponse
Documentation: https://system-bridge.timmo.dev
"""
from .payload import CommandPayload


class CommandResponse(CommandPayload):
    @property
    def success(self):
        return self.attributes.get("success", True)

    @property
    def message(self):
        return self.attributes.get("message", "")
