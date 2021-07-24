"""
Class object for Filesystem
Documentation: https://system-bridge.timmo.dev
"""
from typing import Any, Dict, Optional
from .base import BridgeBase


class BlockDevices(BridgeBase):
    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def identifier(self):
        return self.attributes.get("identifier", "")

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def fsType(self):
        return self.attributes.get("fsType", "")

    @property
    def mount(self):
        return self.attributes.get("mount", "")

    @property
    def size(self):
        return self.attributes.get("size", "")

    @property
    def physical(self):
        return self.attributes.get("physical", "")

    @property
    def uuid(self):
        return self.attributes.get("uuid", "")

    @property
    def label(self):
        return self.attributes.get("label", "")

    @property
    def model(self):
        return self.attributes.get("model", "")

    @property
    def serial(self):
        return self.attributes.get("serial", "")

    @property
    def removable(self):
        return self.attributes.get("removable", False)

    @property
    def protocol(self):
        return self.attributes.get("protocol", "")


class DiskLayout(BridgeBase):
    @property
    def device(self):
        return self.attributes.get("device", "")

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def name(self):
        return self.attributes.get("name", "")

    @property
    def vendor(self):
        return self.attributes.get("vendor", "")

    @property
    def size(self):
        return self.attributes.get("size", None)

    @property
    def bytesPerSector(self):
        return self.attributes.get("bytesPerSector", None)

    @property
    def totalCylinders(self):
        return self.attributes.get("totalCylinders", None)

    @property
    def totalHeads(self):
        return self.attributes.get("totalHeads", None)

    @property
    def totalSectors(self):
        return self.attributes.get("totalSectors", None)

    @property
    def totalTracks(self):
        return self.attributes.get("totalTracks", None)

    @property
    def tracksPerCylinder(self):
        return self.attributes.get("tracksPerCylinder", None)

    @property
    def sectorsPerTrack(self):
        return self.attributes.get("sectorsPerTrack", None)

    @property
    def firmwareRevision(self):
        return self.attributes.get("firmwareRevision", "")

    @property
    def serialNum(self):
        return self.attributes.get("serialNum", "")

    @property
    def interfaceType(self):
        return self.attributes.get("interfaceType", "")

    @property
    def smartStatus(self):
        return self.attributes.get("smartStatus", "")

    @property
    def temperature(self):
        return self.attributes.get("temperature", None)


class FsSize(BridgeBase):
    @property
    def fs(self):
        return self.attributes.get("fs", "")

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def size(self):
        return self.attributes.get("size", None)

    @property
    def used(self):
        return self.attributes.get("used", None)

    @property
    def available(self):
        return self.attributes.get("available", None)

    @property
    def use(self):
        return self.attributes.get("use", None)

    @property
    def mount(self):
        return self.attributes.get("mount", "")


class Filesystem(BridgeBase):
    @property
    def blockDevices(self) -> Optional[Dict[str, BlockDevices]]:
        return self.attributes.get("blockDevices", {})

    @property
    def diskLayout(self) -> Optional[Dict[str, DiskLayout]]:
        return self.attributes.get("diskLayout", {})

    @property
    def disksIO(self) -> Optional[Dict[str, Any]]:
        return self.attributes.get("disksIO", "")

    @property
    def fsSize(self) -> Optional[Dict[str, FsSize]]:
        return self.attributes.get("fsSize", {})
