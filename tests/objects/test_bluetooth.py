"""
Generated by generator/generator.py - 2021-02-20 16:50:21.146717
"""
from systembridge.objects.bluetooth import BridgeBluetooth
from tests.responses.bluetooth_fixture import bluetooth_fixture_response

def test_bluetooth(bluetooth_fixture_response):
    obj = BridgeBluetooth(bluetooth_fixture_response)
    assert obj.device == bluetooth_fixture_response['device']
    assert obj.name == bluetooth_fixture_response['name']
    assert obj.manufacturer == bluetooth_fixture_response['manufacturer']
    assert obj.macDevice == bluetooth_fixture_response['macDevice']
    assert obj.macHost == bluetooth_fixture_response['macHost']
    assert obj.batteryPercent == bluetooth_fixture_response['batteryPercent']
    assert obj.type == bluetooth_fixture_response['type']
    assert obj.connected == bluetooth_fixture_response['connected']