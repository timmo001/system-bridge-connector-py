"""
Generated by generator/generator.py - 2021-02-20 16:57:03.395502
"""
import pytest


@pytest.fixture()
def response_fixture_response():
    return {
        "command": "python",
        "arguments": ["-V"],
        "wait": True,
        "success": True,
        "message": "Python 3.9.1",
    }
