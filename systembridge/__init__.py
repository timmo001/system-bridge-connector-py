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
        self._data = {}

    @property
    def audio(self) -> List[Audio]:
        return self._data.audio

    @property
    def battery(self) -> Battery:
        return self._data.battery

    @property
    def bluetooth(self) -> Bluetooth:
        return self._data.bluetooth

    @property
    def cpu(self) -> Cpu:
        return self._data.cpu

    @property
    def filesystem(self) -> Filesystem:
        return self._data.filesystem

    @property
    def graphics(self) -> Graphics:
        return self._data.graphics

    @property
    def information(self) -> Information:
        return self._data.information

    @property
    def memory(self) -> Memory:
        return self._data.memory

    @property
    def network(self) -> Network:
        return self._data.network

    @property
    def os(self) -> Os:
        return self._data.os

    @property
    def system(self) -> System:
        return self._data.system

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
        self._data.audio = [
            Audio(audio) for audio in await self.async_get("/audio") or []
        ]
        self._data.audio

    async def async_get_battery(self) -> Battery:
        """Get battery information"""
        self._data.battery = Battery(await self.async_get("/battery"))
        return self._data.battery

    async def async_get_bluetooth(self) -> Bluetooth:
        """Get bluetooth information"""
        self._data.bluetooth = Bluetooth(await self.async_get("/bluetooth"))
        return self._data.bluetooth

    async def async_send_command(self, payload: CommandPayload) -> CommandResponse:
        """Get cpu information"""
        return CommandResponse(await self.async_get("/command", payload))

    async def async_get_cpu(self) -> Cpu:
        """Get cpu information"""
        self._data.cpu = Cpu(await self.async_get("/cpu"))
        return self._data.cpu

    async def async_get_filesystem(self) -> Filesystem:
        """Get filesystem information"""
        self._data.filesystem = Filesystem(await self.async_get("/filesystem"))
        return self._data.filesystem

    async def async_get_graphics(self) -> Graphics:
        """Get graphics information"""
        self._data.graphics = Graphics(await self.async_get("/graphics"))
        return self._data.graphics

    async def async_get_information(self) -> Information:
        """Get information"""
        self._data.information = Information(await self.async_get("/information"))
        return self._data.information

    async def async_get_memory(self) -> Memory:
        """Get memory information"""
        self._data.memory = Memory(await self.async_get("/memory"))
        return self._data.memory

    async def async_get_network(self) -> Network:
        """Get network information"""
        self._data.network = Network(await self.async_get("/network"))
        return self._data.network

    async def async_get_os(self) -> Os:
        """Get os information"""
        self._data.os = Os(await self.async_get("/os"))
        return self._data.os

    async def async_get_system(self) -> System:
        """Get system information"""
        self._data.system = System(await self.async_get("/system"))
        return self._data.system
