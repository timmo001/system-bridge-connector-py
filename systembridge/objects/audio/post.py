"""
Class object for AudioPostPayload and AudioPostResponse
Documentation: https://system-bridge.timmo.dev
"""
from typing import Optional
from ..base import BridgeBase


class AudioPostPayload(BridgeBase):
    @property
    def backgroundColor(self) -> Optional[str]:
        return self.attributes.get("backgroundColor", "")

    @property
    def hidden(self) -> Optional[bool]:
        return self.attributes.get("hidden", False)

    @property
    def opacity(self) -> Optional[str]:
        return self.attributes.get("backgroundColor", "")

    @property
    def path(self) -> Optional[str]:
        return self.attributes.get("path", "")

    @property
    def transparent(self) -> Optional[str]:
        return self.attributes.get("transparent", False)

    @property
    def url(self) -> Optional[str]:
        return self.attributes.get("url", "")

    @property
    def x(self) -> Optional[float]:
        return self.attributes.get("x", 0.0)

    @property
    def y(self) -> Optional[float]:
        return self.attributes.get("y", 0.0)


class AudioPostResponse(AudioPostPayload):
    def type(self) -> str:
        return self.attributes.get("type", "audio")

    @property
    def url(self) -> str:
        return self.attributes.get("url", "")
