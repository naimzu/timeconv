from timeconv import (
    second_to_minute,
    second_to_hour,
    minute_to_hour,
    minute_to_second,
    hour_to_minute,
    hour_to_second,
)


def test_second_to_minute():
    assert second_to_minute(120) == 2.0
    assert second_to_minute(90) == 1.5
    assert second_to_minute(1) == 0.01667


def test_second_to_hour():
    assert second_to_hour(3600) == 1.0
    assert second_to_hour(1800) == 0.5
    assert second_to_hour(1) == 0.00028


def test_minute_to_hour():
    assert minute_to_hour(60) == 1.0
    assert minute_to_hour(30) == 0.5
    assert minute_to_hour(1) == 0.01667


def test_minute_to_second():
    assert minute_to_second(1) == 60
    assert minute_to_second(2.5) == 150.0
    assert minute_to_second(0.1) == 6.0


def test_hour_to_minute():
    assert hour_to_minute(1) == 60
    assert hour_to_minute(2.5) == 150.0
    assert hour_to_minute(0.5) == 30.0


def test_hour_to_second():
    assert hour_to_second(1) == 3600
    assert hour_to_second(2) == 7200
    assert hour_to_second(0.5) == 1800.0