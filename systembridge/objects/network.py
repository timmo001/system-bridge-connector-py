"""
Class object for Network
Documentation: https://system-bridge.timmo.dev
"""
from typing import Dict, Optional
from .base import BridgeBase


class Connections(BridgeBase):
    @property
    def protocol(self):
        return self.attributes.get("protocol", "")

    @property
    def localAddress(self):
        return self.attributes.get("localAddress", "")

    @property
    def localPort(self):
        return self.attributes.get("localPort", "")

    @property
    def peerAddress(self):
        return self.attributes.get("peerAddress", "")

    @property
    def peerPort(self):
        return self.attributes.get("peerPort", "")

    @property
    def state(self):
        return self.attributes.get("state", "")

    @property
    def pid(self):
        return self.attributes.get("pid", "")

    @property
    def process(self):
        return self.attributes.get("process", "")


class Interface(BridgeBase):
    @property
    def iface(self):
        return self.attributes.get("iface", "")

    @property
    def ifaceName(self):
        return self.attributes.get("ifaceName", "")

    @property
    def ip4(self):
        return self.attributes.get("ip4", "")

    @property
    def ip4subnet(self):
        return self.attributes.get("ip4subnet", "")

    @property
    def ip6(self):
        return self.attributes.get("ip6", "")

    @property
    def ip6subnet(self):
        return self.attributes.get("ip6subnet", "")

    @property
    def mac(self):
        return self.attributes.get("mac", "")

    @property
    def internal(self):
        return self.attributes.get("internal", False)

    @property
    def virtual(self):
        return self.attributes.get("virtual", False)

    @property
    def operstate(self):
        return self.attributes.get("operstate", "")

    @property
    def type(self):
        return self.attributes.get("type", "")

    @property
    def duplex(self):
        return self.attributes.get("duplex", "")

    @property
    def mtu(self):
        return self.attributes.get("mtu", "")

    @property
    def speed(self):
        return self.attributes.get("speed", None)

    @property
    def dhcp(self):
        return self.attributes.get("dhcp", "")

    @property
    def dnsSuffix(self):
        return self.attributes.get("dnsSuffix", "")

    @property
    def ieee8021xAuth(self):
        return self.attributes.get("ieee8021xAuth", "")

    @property
    def ieee8021xState(self):
        return self.attributes.get("ieee8021xState", "")

    @property
    def carrierChanges(self):
        return self.attributes.get("carrierChanges", None)


class Stat(BridgeBase):
    @property
    def iface(self):
        return self.attributes.get("iface", "")

    @property
    def operstate(self):
        return self.attributes.get("operstate", "")

    @property
    def rx_bytes(self):
        return self.attributes.get("rx_bytes", None)

    @property
    def rx_dropped(self):
        return self.attributes.get("rx_dropped", None)

    @property
    def rx_errors(self):
        return self.attributes.get("rx_errors", None)

    @property
    def tx_bytes(self):
        return self.attributes.get("tx_bytes", None)

    @property
    def tx_dropped(self):
        return self.attributes.get("tx_dropped", None)

    @property
    def tx_errors(self):
        return self.attributes.get("tx_errors", None)

    @property
    def rx_sec(self):
        return self.attributes.get("rx_sec", None)

    @property
    def tx_sec(self):
        return self.attributes.get("tx_sec", None)

    @property
    def ms(self):
        return self.attributes.get("ms", None)


class Network(BridgeBase):
    @property
    def connections(self):
        return [Connections(x) for x in self.attributes.get("connections", [])]

    @property
    def gatewayDefault(self):
        return self.attributes.get("gatewayDefault", "")

    @property
    def interfaceDefault(self):
        return self.attributes.get("interfaceDefault", "")

    @property
    def interfaces(self) -> Optional[Dict[str, Interface]]:
        return self.attributes.get("interfaces", {})

    @property
    def stats(self) -> Optional[Dict[str, Stat]]:
        return self.attributes.get("stats", {})
