"""
Generated by generator/generator.py - 2021-02-20 17:07:56.628512
"""
from systembridge.objects.memory import Memory
from tests.fixtrues.memory_fixtrue import memory_fixtrue_response


def test_memory(memory_fixtrue_response):
    obj = Memory(memory_fixtrue_response)
    assert obj.total == memory_fixtrue_response["total"]
    assert obj.free == memory_fixtrue_response["free"]
    assert obj.used == memory_fixtrue_response["used"]
    assert obj.active == memory_fixtrue_response["active"]
    assert obj.available == memory_fixtrue_response["available"]
    assert obj.buffers == memory_fixtrue_response["buffers"]
    assert obj.cached == memory_fixtrue_response["cached"]
    assert obj.slab == memory_fixtrue_response["slab"]
    assert obj.buffcache == memory_fixtrue_response["buffcache"]
    assert obj.swaptotal == memory_fixtrue_response["swaptotal"]
    assert obj.swapused == memory_fixtrue_response["swapused"]
    assert obj.swapfree == memory_fixtrue_response["swapfree"]
    assert obj.layout[0].size == memory_fixtrue_response["layout"][0]["size"]
    assert obj.layout[0].bank == memory_fixtrue_response["layout"][0]["bank"]
    assert obj.layout[0].type == memory_fixtrue_response["layout"][0]["type"]
    assert obj.layout[0].ecc == memory_fixtrue_response["layout"][0]["ecc"]
    assert (
        obj.layout[0].clockSpeed == memory_fixtrue_response["layout"][0]["clockSpeed"]
    )
    assert (
        obj.layout[0].formFactor == memory_fixtrue_response["layout"][0]["formFactor"]
    )
    assert (
        obj.layout[0].manufacturer
        == memory_fixtrue_response["layout"][0]["manufacturer"]
    )
    assert obj.layout[0].partNum == memory_fixtrue_response["layout"][0]["partNum"]
    assert obj.layout[0].serialNum == memory_fixtrue_response["layout"][0]["serialNum"]
    assert (
        obj.layout[0].voltageConfigured
        == memory_fixtrue_response["layout"][0]["voltageConfigured"]
    )
    assert (
        obj.layout[0].voltageMin == memory_fixtrue_response["layout"][0]["voltageMin"]
    )
    assert (
        obj.layout[0].voltageMax == memory_fixtrue_response["layout"][0]["voltageMax"]
    )
