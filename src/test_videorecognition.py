import pytest

from VideoRecognotion import VideoRecognition

def test_getcameradevices():
    assert VideoRecognition.getCameraDevices() == [0]
def test_vid2lines():
    assert VideoRecognition.Vid2Lines(0) == None