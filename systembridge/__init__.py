"""Bridge: Init"""
from aiohttp import ClientResponse
from typing import Any, List

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

    async def async_get(self, path: str) -> Any:
        """Generic Getter"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}{path}",
            headers={**BASE_HEADERS, "api-key": self._api_key},
        )
        return response.json()

    async def async_post(self, path: str, payload: Any) -> Any:
        """Generic Getter"""
        response: ClientResponse = await self._client.get(
            f"{self._base_url}{path}",
            headers={**BASE_HEADERS, "api-key": self._api_key},
            json=payload,
        )
        return response.json()

    async def async_get_audio(self) -> List[Audio]:
        """Get audio information"""
        return [Audio(audio) for audio in await self.async_get("/audio") or []]

    async def async_get_battery(self) -> Battery:
        """Get battery information"""
        return Battery(await self.async_get("/battery"))

    async def async_get_bluetooth(self) -> Bluetooth:
        """Get bluetooth information"""
        return Bluetooth(await self.async_get("/bluetooth"))

    async def async_send_command(self, payload: CommandPayload) -> CommandResponse:
        """Get cpu information"""
        return CommandResponse(await self.async_get("/command", payload))

    async def async_get_cpu(self) -> Cpu:
        """Get cpu information"""
        return Cpu(await self.async_get("/cpu"))

    async def async_get_filesystem(self) -> Filesystem:
        """Get filesystem information"""
        return Filesystem(await self.async_get("/filesystem"))

    async def async_get_graphics(self) -> Graphics:
        """Get graphics information"""
        return Graphics(await self.async_get("/graphics"))

    async def async_get_information(self) -> Information:
        """Get information"""
        return Information(await self.async_get("/information"))

    async def async_get_memory(self) -> Memory:
        """Get memory information"""
        return Memory(await self.async_get("/memory"))

    async def async_get_network(self) -> Network:
        """Get network information"""
        return Network(await self.async_get("/network"))

    async def async_get_os(self) -> Os:
        """Get os information"""
        return Os(await self.async_get("/os"))

    async def async_get_system(self) -> System:
        """Get system information"""
        return System(await self.async_get("/system"))
