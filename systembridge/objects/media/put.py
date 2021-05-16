"""
Class object for MediaPutResponse
Documentation: https://system-bridge.timmo.dev
"""
from ..base import BridgeBase


class MediaPutResponse(BridgeBase):
    @property
    def successful(self) -> bool:
        return self.attributes.get("successful", False)
