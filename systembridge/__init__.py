"""Bridge: Init"""
from aiohttp import ClientResponse
from typing import List

from .client import BridgeClient
from .objects.base import BridgeBase
from .objects.audio import Audio
from .objects.battery import Battery
from .objects.bluetooth import Bluetooth
from .objects.command.payload import CommandPayload
from .objects.command.response import CommandResponse
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
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/audio",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return [Audio(audio) for audio in await response.json() or []]

    async def async_get_battery(self) -> Battery:
        """Get battery information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/battery",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Battery(await response.json())

    async def async_get_bluetooth(self) -> Bluetooth:
        """Get bluetooth information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/bluetooth",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Bluetooth(await response.json())

    async def async_send_command(self, payload: CommandPayload) -> CommandResponse:
        """Get cpu information"""
        response: ClientResponse = await self._client.post(
            f"{self._base_url}/command",
            headers={**BASE_HEADERS, "api-key": self._api_key},
            json=payload,
        )
        return CommandResponse(await response.json())

    async def async_get_cpu(self) -> Cpu:
        """Get cpu information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/cpu",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Cpu(await response.json())

    async def async_get_filesystem(self) -> Filesystem:
        """Get filesystem information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/filesystem",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Filesystem(await response.json())

    async def async_get_graphics(self) -> Graphics:
        """Get graphics information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/graphics",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Graphics(await response.json())

    async def async_get_information(self) -> Information:
        """Get information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/information",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Information(await response.json())

    async def async_get_memory(self) -> Memory:
        """Get memory information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/memory",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Memory(await response.json())

    async def async_get_network(self) -> Network:
        """Get network information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/network",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Network(await response.json())

    async def async_get_os(self) -> Os:
        """Get os information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/os",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return Os(await response.json())

    async def async_get_system(self) -> System:
        """Get system information"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}/system",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return System(await response.json())
