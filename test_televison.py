# test_television.py
import pytest
from television import Television


def test_init():
    tv = Television()
    assert tv._status is False
    assert tv._muted is False
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL


def test_power():
    tv = Television()
    tv.power()
    assert tv._status is True
    tv.power()
    assert tv._status is False


def test_mute():
    tv = Television()
    tv.mute()
    assert tv._muted is True
    tv.mute()
    assert tv._muted is False


if __name__ == '__main__':
    pytest.main()
