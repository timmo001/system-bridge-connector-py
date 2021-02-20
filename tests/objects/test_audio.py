"""
Generated by generator/generator.py - 2021-02-20 16:48:42.854477
"""
from systembridge.objects.audio import BridgeAudio
from tests.responses.audio_fixture import audio_fixture_response

def test_audio(audio_fixture_response):
    obj = BridgeAudio(audio_fixture_response)
    assert obj.id == audio_fixture_response['id']
    assert obj.name == audio_fixture_response['name']
    assert obj.manufacturer == audio_fixture_response['manufacturer']
    assert obj.revision == audio_fixture_response['revision']
    assert obj.driver == audio_fixture_response['driver']
    assert obj.default == audio_fixture_response['default']
    assert obj.channel == audio_fixture_response['channel']
    assert obj.type == audio_fixture_response['type']
    assert obj.in == audio_fixture_response['in']
    assert obj.out == audio_fixture_response['out']
    assert obj.status == audio_fixture_response['status']
