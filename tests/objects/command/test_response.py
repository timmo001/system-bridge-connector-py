"""
Generated by generator/generator.py - 2021-02-20 16:57:03.395502
"""
from systembridge.objects.command.response import Response
from tests.responses.command.response_fixture import response_fixture_response

def test_response(response_fixture_response):
    obj = Response(response_fixture_response)
    assert obj.command == response_fixture_response['command']
    assert obj.arguments[0] == response_fixture_response['arguments'][0]
    assert obj.wait == response_fixture_response['wait']
    assert obj.success == response_fixture_response['success']
    assert obj.message == response_fixture_response['message']