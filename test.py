"""Test class for System Bridge"""
from __future__ import annotations
from systembridge.objects.events import Event
from aiohttp.client import ClientSession

import asyncio
import async_timeout

from systembridge import Bridge
from systembridge.client import BridgeClient

HOST = "localhost"
PORT = 9170
API_KEY = ""


async def get_data() -> tuple[BridgeClient, int]:
    async with ClientSession() as session:
        client = Bridge(
            BridgeClient(session),
            f"http://{HOST}:{PORT}",
            API_KEY,
        )
        async with async_timeout.timeout(60):
            await asyncio.gather(
                *[
                    client.async_get_audio(),
                    client.async_get_battery(),
                    client.async_get_bluetooth(),
                    client.async_get_cpu(),
                    client.async_get_display(),
                    client.async_get_filesystem(),
                    client.async_get_graphics(),
                    client.async_get_media(),
                    client.async_get_memory(),
                    client.async_get_network(),
                    client.async_get_os(),
                    client.async_get_processes(),
                    client.async_get_settings(),
                    client.async_get_system(),
                ]
            )
        return client, (await client.async_get_setting("network", "wsPort")).value


async def print_event(event: Event):
    print(event)


async def main():
    client, wsPort = await get_data()

    print()
    print("Results")
    print()
    print(client.audio)
    # print(client.audio.__dict__)
    # print()
    print(client.bluetooth)
    # print(client.bluetooth.__dict__)
    # print()
    print(client.battery)
    # print(client.battery.__dict__)
    # print()
    print(client.cpu)
    # print(client.cpu.__dict__)
    # print()
    print(client.display)
    # print(client.display.__dict__)
    # print()
    print(client.filesystem)
    # print(client.filesystem.__dict__)
    # print()
    print(client.graphics)
    # print(client.graphics.__dict__)
    # print()
    print(client.media)
    # print(client.media.__dict__)
    # print()
    print(client.memory)
    # print(client.memory.__dict__)
    # print()
    print(client.network)
    # print(client.network.__dict__)
    # print()
    print(client.os)
    # print(client.os.__dict__)
    # print()
    print(client.processes)
    # print(client.processes.__dict__)
    # print()
    print(client.settings)
    # for setting in client.settings:
    #     print(setting.__dict__)
    #     print(setting.key)
    #     print(setting.name)
    #     print(setting.value)
    # print()
    print(client.system)
    # print(client.system.__dict__)

    print()
    print("WebSocket")
    print()

    await client.async_connect_websocket(HOST, wsPort)
    await client.async_send_event("test", "text")
    await client.listen_for_events(print_event)


asyncio.run(main())
