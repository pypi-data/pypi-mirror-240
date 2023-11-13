import pytest
from src.sec2time import convert_seconds



def test_convert_seconds():
    assert convert_seconds(7500) == "2 hours 5 minutes"
    assert convert_seconds(3600) == "1 hour"
    assert convert_seconds(60) == "1 minute"
    assert convert_seconds(1) == "1 second"