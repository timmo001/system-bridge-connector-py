"""Test class for System Bridge"""
import asyncio
import async_timeout

from aiohttp.client import ClientSession

from systembridge import Bridge
from systembridge.client import BridgeClient

HOST = "localhost"
PORT = 9170
API_KEY = ""


async def get_data() -> Bridge:
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
                    client.async_get_memory(),
                    client.async_get_network(),
                    client.async_get_os(),
                    client.async_get_processes(),
                    client.async_get_settings(),
                    client.async_get_system(),
                ]
            )
            # print((await client.async_get_setting("network", "wsPort")).value)
        return client


async def main():
    client = await get_data()

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


asyncio.run(main())
