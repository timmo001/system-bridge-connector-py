"""
Class object for VideoPutPayload and VideoPutResponse
Documentation: https://system-bridge.timmo.dev
"""
from typing import Union

from ..base import BridgeBase


class VideoPutPayload(BridgeBase):
    @property
    def value(self) -> Union[bool, float]:
        return self.attributes.get("value", True)


class VideoPutResponse(BridgeBase):
    @property
    def successful(self) -> bool:
        return self.attributes.get("successful", False)
