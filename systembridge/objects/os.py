"""
Class object for Os
Documentation: https://system-bridge.timmo.dev
"""
from .base import BridgeBase


class Users(BridgeBase):
    @property
    def user(self):
        return self.attributes.get("user", "")

    @property
    def tty(self):
        return self.attributes.get("tty", "")

    @property
    def date(self):
        return self.attributes.get("date", "")

    @property
    def time(self):
        return self.attributes.get("time", "")

    @property
    def ip(self):
        return self.attributes.get("ip", "")

    @property
    def command(self):
        return self.attributes.get("command", "")


class Os(BridgeBase):
    @property
    def platform(self):
        return self.attributes.get("platform", "")

    @property
    def distro(self):
        return self.attributes.get("distro", "")

    @property
    def release(self):
        return self.attributes.get("release", "")

    @property
    def codename(self):
        return self.attributes.get("codename", "")

    @property
    def kernel(self):
        return self.attributes.get("kernel", "")

    @property
    def arch(self):
        return self.attributes.get("arch", "")

    @property
    def hostname(self):
        return self.attributes.get("hostname", "")

    @property
    def idle_time(self):
        return self.attributes.get("idleTime", "")

    @property
    def fqdn(self):
        return self.attributes.get("fqdn", "")

    @property
    def codepage(self):
        return self.attributes.get("codepage", "")

    @property
    def logofile(self):
        return self.attributes.get("logofile", "")

    @property
    def serial(self):
        return self.attributes.get("serial", "")

    @property
    def build(self):
        return self.attributes.get("build", "")

    @property
    def servicepack(self):
        return self.attributes.get("servicepack", "")

    @property
    def uefi(self):
        return self.attributes.get("uefi", False)

    @property
    def hypervisor(self):
        return self.attributes.get("hypervisor", True)

    @property
    def remoteSession(self):
        return self.attributes.get("remoteSession", False)

    @property
    def users(self):
        return [Users(x) for x in self.attributes.get("users", [])]
