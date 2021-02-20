"""
Generated by generator/generator.py - 2021-02-20 17:07:18.274493
"""
from systembridge.objects.graphics import Graphics
from tests.fixtrues.graphics_fixtrue import graphics_fixtrue_response


def test_graphics(graphics_fixtrue_response):
    obj = Graphics(graphics_fixtrue_response)
    assert (
        obj.controllers[0].vendor
        == graphics_fixtrue_response["controllers"][0]["vendor"]
    )
    assert (
        obj.controllers[0].model == graphics_fixtrue_response["controllers"][0]["model"]
    )
    assert obj.controllers[0].bus == graphics_fixtrue_response["controllers"][0]["bus"]
    assert (
        obj.controllers[0].vram == graphics_fixtrue_response["controllers"][0]["vram"]
    )
    assert (
        obj.controllers[0].vramDynamic
        == graphics_fixtrue_response["controllers"][0]["vramDynamic"]
    )
    assert (
        obj.controllers[0].subDeviceId
        == graphics_fixtrue_response["controllers"][0]["subDeviceId"]
    )
    assert (
        obj.controllers[0].driverVersion
        == graphics_fixtrue_response["controllers"][0]["driverVersion"]
    )
    assert (
        obj.controllers[0].name == graphics_fixtrue_response["controllers"][0]["name"]
    )
    assert (
        obj.controllers[0].pciBus
        == graphics_fixtrue_response["controllers"][0]["pciBus"]
    )
    assert (
        obj.controllers[0].memoryTotal
        == graphics_fixtrue_response["controllers"][0]["memoryTotal"]
    )
    assert (
        obj.controllers[0].memoryUsed
        == graphics_fixtrue_response["controllers"][0]["memoryUsed"]
    )
    assert (
        obj.controllers[0].memoryFree
        == graphics_fixtrue_response["controllers"][0]["memoryFree"]
    )
    assert (
        obj.controllers[0].utilizationGpu
        == graphics_fixtrue_response["controllers"][0]["utilizationGpu"]
    )
    assert (
        obj.controllers[0].utilizationMemory
        == graphics_fixtrue_response["controllers"][0]["utilizationMemory"]
    )
    assert (
        obj.controllers[0].temperatureGpu
        == graphics_fixtrue_response["controllers"][0]["temperatureGpu"]
    )
    assert (
        obj.controllers[0].powerDraw
        == graphics_fixtrue_response["controllers"][0]["powerDraw"]
    )
    assert (
        obj.controllers[0].powerLimit
        == graphics_fixtrue_response["controllers"][0]["powerLimit"]
    )
    assert (
        obj.controllers[0].clockCore
        == graphics_fixtrue_response["controllers"][0]["clockCore"]
    )
    assert (
        obj.controllers[0].clockMemory
        == graphics_fixtrue_response["controllers"][0]["clockMemory"]
    )
    assert obj.displays[0].vendor == graphics_fixtrue_response["displays"][0]["vendor"]
    assert obj.displays[0].model == graphics_fixtrue_response["displays"][0]["model"]
    assert (
        obj.displays[0].deviceName
        == graphics_fixtrue_response["displays"][0]["deviceName"]
    )
    assert obj.displays[0].main == graphics_fixtrue_response["displays"][0]["main"]
    assert (
        obj.displays[0].builtin == graphics_fixtrue_response["displays"][0]["builtin"]
    )
    assert (
        obj.displays[0].connection
        == graphics_fixtrue_response["displays"][0]["connection"]
    )
    assert (
        obj.displays[0].resolutionX
        == graphics_fixtrue_response["displays"][0]["resolutionX"]
    )
    assert (
        obj.displays[0].resolutionY
        == graphics_fixtrue_response["displays"][0]["resolutionY"]
    )
    assert obj.displays[0].sizeX == graphics_fixtrue_response["displays"][0]["sizeX"]
    assert obj.displays[0].sizeY == graphics_fixtrue_response["displays"][0]["sizeY"]
    assert (
        obj.displays[0].pixelDepth
        == graphics_fixtrue_response["displays"][0]["pixelDepth"]
    )
    assert (
        obj.displays[0].currentResX
        == graphics_fixtrue_response["displays"][0]["currentResX"]
    )
    assert (
        obj.displays[0].currentResY
        == graphics_fixtrue_response["displays"][0]["currentResY"]
    )
    assert (
        obj.displays[0].positionX
        == graphics_fixtrue_response["displays"][0]["positionX"]
    )
    assert (
        obj.displays[0].positionY
        == graphics_fixtrue_response["displays"][0]["positionY"]
    )