"""
Generated by generator/generator.py - 2021-02-20 17:05:47.607534
"""
from systembridge.objects.filesystem import Filesystem
from tests.fixtrues.filesystem_fixtrue import filesystem_fixtrue_response


def test_filesystem(filesystem_fixtrue_response):
    obj = Filesystem(filesystem_fixtrue_response)
    assert (
        obj.blockDevices[0].name
        == filesystem_fixtrue_response["blockDevices"][0]["name"]
    )
    assert (
        obj.blockDevices[0].identifier
        == filesystem_fixtrue_response["blockDevices"][0]["identifier"]
    )
    assert (
        obj.blockDevices[0].type
        == filesystem_fixtrue_response["blockDevices"][0]["type"]
    )
    assert (
        obj.blockDevices[0].fsType
        == filesystem_fixtrue_response["blockDevices"][0]["fsType"]
    )
    assert (
        obj.blockDevices[0].mount
        == filesystem_fixtrue_response["blockDevices"][0]["mount"]
    )
    assert (
        obj.blockDevices[0].size
        == filesystem_fixtrue_response["blockDevices"][0]["size"]
    )
    assert (
        obj.blockDevices[0].physical
        == filesystem_fixtrue_response["blockDevices"][0]["physical"]
    )
    assert (
        obj.blockDevices[0].uuid
        == filesystem_fixtrue_response["blockDevices"][0]["uuid"]
    )
    assert (
        obj.blockDevices[0].label
        == filesystem_fixtrue_response["blockDevices"][0]["label"]
    )
    assert (
        obj.blockDevices[0].model
        == filesystem_fixtrue_response["blockDevices"][0]["model"]
    )
    assert (
        obj.blockDevices[0].serial
        == filesystem_fixtrue_response["blockDevices"][0]["serial"]
    )
    assert (
        obj.blockDevices[0].removable
        == filesystem_fixtrue_response["blockDevices"][0]["removable"]
    )
    assert (
        obj.blockDevices[0].protocol
        == filesystem_fixtrue_response["blockDevices"][0]["protocol"]
    )
    assert (
        obj.diskLayout[0].device
        == filesystem_fixtrue_response["diskLayout"][0]["device"]
    )
    assert (
        obj.diskLayout[0].type == filesystem_fixtrue_response["diskLayout"][0]["type"]
    )
    assert (
        obj.diskLayout[0].name == filesystem_fixtrue_response["diskLayout"][0]["name"]
    )
    assert (
        obj.diskLayout[0].vendor
        == filesystem_fixtrue_response["diskLayout"][0]["vendor"]
    )
    assert (
        obj.diskLayout[0].size == filesystem_fixtrue_response["diskLayout"][0]["size"]
    )
    assert (
        obj.diskLayout[0].bytesPerSector
        == filesystem_fixtrue_response["diskLayout"][0]["bytesPerSector"]
    )
    assert (
        obj.diskLayout[0].totalCylinders
        == filesystem_fixtrue_response["diskLayout"][0]["totalCylinders"]
    )
    assert (
        obj.diskLayout[0].totalHeads
        == filesystem_fixtrue_response["diskLayout"][0]["totalHeads"]
    )
    assert (
        obj.diskLayout[0].totalSectors
        == filesystem_fixtrue_response["diskLayout"][0]["totalSectors"]
    )
    assert (
        obj.diskLayout[0].totalTracks
        == filesystem_fixtrue_response["diskLayout"][0]["totalTracks"]
    )
    assert (
        obj.diskLayout[0].tracksPerCylinder
        == filesystem_fixtrue_response["diskLayout"][0]["tracksPerCylinder"]
    )
    assert (
        obj.diskLayout[0].sectorsPerTrack
        == filesystem_fixtrue_response["diskLayout"][0]["sectorsPerTrack"]
    )
    assert (
        obj.diskLayout[0].firmwareRevision
        == filesystem_fixtrue_response["diskLayout"][0]["firmwareRevision"]
    )
    assert (
        obj.diskLayout[0].serialNum
        == filesystem_fixtrue_response["diskLayout"][0]["serialNum"]
    )
    assert (
        obj.diskLayout[0].interfaceType
        == filesystem_fixtrue_response["diskLayout"][0]["interfaceType"]
    )
    assert (
        obj.diskLayout[0].smartStatus
        == filesystem_fixtrue_response["diskLayout"][0]["smartStatus"]
    )
    assert (
        obj.diskLayout[0].temperature
        == filesystem_fixtrue_response["diskLayout"][0]["temperature"]
    )
    assert obj.disksIO == filesystem_fixtrue_response["disksIO"]
    assert obj.fsSize[0].fs == filesystem_fixtrue_response["fsSize"][0]["fs"]
    assert obj.fsSize[0].type == filesystem_fixtrue_response["fsSize"][0]["type"]
    assert obj.fsSize[0].size == filesystem_fixtrue_response["fsSize"][0]["size"]
    assert obj.fsSize[0].used == filesystem_fixtrue_response["fsSize"][0]["used"]
    assert (
        obj.fsSize[0].available == filesystem_fixtrue_response["fsSize"][0]["available"]
    )
    assert obj.fsSize[0].use == filesystem_fixtrue_response["fsSize"][0]["use"]
    assert obj.fsSize[0].mount == filesystem_fixtrue_response["fsSize"][0]["mount"]
