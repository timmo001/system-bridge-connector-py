"""
Class object for DisplayPutPayload
Documentation: https://system-bridge.timmo.dev
"""
from typing import Union

from ..base import BridgeBase


class DisplayPutPayload(BridgeBase):
    @property
    def value(self) -> Union[bool, float]:
        return self.attributes.get("value", True)
