"""Bridge: Init"""
from typing import List

from .client import BridgeClient
from .objects.base import BridgeBase
from .objects.audio import Audio
from .objects.battery import Battery
from .objects.bluetooth import Bluetooth
from .objects.command import CommandPayload, CommandResponse
from .objects.cpu import Cpu
from .objects.filesystem import Filesystem
from .objects.graphics import Graphics
from .objects.information import Information
from .objects.memory import Memory
from .objects.network import Network
from .objects.os import Os
from .objects.system import System

BASE_HEADERS = {"Accept": "application/json"}


class Bridge(BridgeBase):
    """Main class for Bridge."""

    def __init__(self, client: BridgeClient, base_url: str, api_key: str) -> None:
        """Initialize the token manager class."""
        self._client = client
        self._base_url = base_url
        self._api_key = api_key

    async def async_get_audio(self) -> List[Audio]:
        """Get audio information"""
        return self._client.get(
            f"{self._base_url}/audio",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_battery(self) -> Battery:
        """Get battery information"""
        return self._client.get(
            f"{self._base_url}/battery",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_bluetooth(self) -> Bluetooth:
        """Get bluetooth information"""
        return self._client.get(
            f"{self._base_url}/bluetooth",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_send_command(self, payload: CommandPayload) -> CommandResponse:
        """Get cpu information"""
        return self._client.post(
            f"{self._base_url}/command",
            headers={**BASE_HEADERS, "api-key": self._api_key},
            json=payload,
        )

    async def async_get_cpu(self) -> Cpu:
        """Get cpu information"""
        return self._client.get(
            f"{self._base_url}/cpu",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_filesystem(self) -> Filesystem:
        """Get filesystem information"""
        return self._client.get(
            f"{self._base_url}/filesystem",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_graphics(self) -> Graphics:
        """Get graphics information"""
        return self._client.get(
            f"{self._base_url}/graphics",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_information(self) -> Information:
        """Get information"""
        return self._client.get(
            f"{self._base_url}/information",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_memory(self) -> Memory:
        """Get memory information"""
        return self._client.get(
            f"{self._base_url}/memory",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_network(self) -> Network:
        """Get network information"""
        return self._client.get(
            f"{self._base_url}/network",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_os(self) -> Os:
        """Get os information"""
        return self._client.get(
            f"{self._base_url}/os",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )

    async def async_get_system(self) -> System:
        """Get system information"""
        return self._client.get(
            f"{self._base_url}/system",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
