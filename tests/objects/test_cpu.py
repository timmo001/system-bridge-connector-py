"""
Generated by generator/generator.py - 2021-02-20 17:02:07.950442
"""
from systembridge.objects.cpu import Cpu
from tests.fixtrues.cpu_fixtrue import cpu_fixtrue_response

def test_cpu(cpu_fixtrue_response):
    obj = Cpu(cpu_fixtrue_response)
    assert obj.cache.l1d == cpu_fixtrue_response['cache']['l1d']
    assert obj.cache.l1i == cpu_fixtrue_response['cache']['l1i']
    assert obj.cache.l2 == cpu_fixtrue_response['cache']['l2']
    assert obj.cache.l3 == cpu_fixtrue_response['cache']['l3']
    assert obj.cpu.manufacturer == cpu_fixtrue_response['cpu']['manufacturer']
    assert obj.cpu.brand == cpu_fixtrue_response['cpu']['brand']
    assert obj.cpu.vendor == cpu_fixtrue_response['cpu']['vendor']
    assert obj.cpu.family == cpu_fixtrue_response['cpu']['family']
    assert obj.cpu.model == cpu_fixtrue_response['cpu']['model']
    assert obj.cpu.stepping == cpu_fixtrue_response['cpu']['stepping']
    assert obj.cpu.revision == cpu_fixtrue_response['cpu']['revision']
    assert obj.cpu.voltage == cpu_fixtrue_response['cpu']['voltage']
    assert obj.cpu.speed == cpu_fixtrue_response['cpu']['speed']
    assert obj.cpu.speedMin == cpu_fixtrue_response['cpu']['speedMin']
    assert obj.cpu.speedMax == cpu_fixtrue_response['cpu']['speedMax']
    assert obj.cpu.governor == cpu_fixtrue_response['cpu']['governor']
    assert obj.cpu.cores == cpu_fixtrue_response['cpu']['cores']
    assert obj.cpu.physicalCores == cpu_fixtrue_response['cpu']['physicalCores']
    assert obj.cpu.processors == cpu_fixtrue_response['cpu']['processors']
    assert obj.cpu.socket == cpu_fixtrue_response['cpu']['socket']
    assert obj.cpu.flags == cpu_fixtrue_response['cpu']['flags']
    assert obj.cpu.virtualization == cpu_fixtrue_response['cpu']['virtualization']
    assert obj.cpu.cache.l1d == cpu_fixtrue_response['cpu']['cache']['l1d']
    assert obj.cpu.cache.l1i == cpu_fixtrue_response['cpu']['cache']['l1i']
    assert obj.cpu.cache.l2 == cpu_fixtrue_response['cpu']['cache']['l2']
    assert obj.cpu.cache.l3 == cpu_fixtrue_response['cpu']['cache']['l3']
    assert obj.currentSpeed.min == cpu_fixtrue_response['currentSpeed']['min']
    assert obj.currentSpeed.max == cpu_fixtrue_response['currentSpeed']['max']
    assert obj.currentSpeed.avg == cpu_fixtrue_response['currentSpeed']['avg']
    assert obj.currentSpeed.cores == cpu_fixtrue_response['currentSpeed']['cores']
    assert obj.temperature.main == cpu_fixtrue_response['temperature']['main']
    assert obj.temperature.max == cpu_fixtrue_response['temperature']['max']
