from timeconv import (
    second_to_minute,
    second_to_hour,
    minute_to_hour,
    minute_to_second,
    hour_to_minute,
    hour_to_second,
)

def test_second_to_minute_under_60(capsys):
    second_to_minute(45.678)
    captured = capsys.readouterr()
    assert captured.out == "45.68 second(s)\n"

def test_second_to_minute_over_60(capsys):
    second_to_minute(125)
    captured = capsys.readouterr()
    assert captured.out == "2 minute(s) : 5 second(s)\n"

def test_second_to_hour_days(capsys):
    second_to_hour(90061)
    captured = capsys.readouterr()
    assert captured.out == "1 day(s) : 1 hour(s) : 1 minute(s) : 1 second(s)\n"

def test_second_to_hour_hours(capsys):
    second_to_hour(3661)
    captured = capsys.readouterr()
    assert captured.out == "1 hour(s) : 1 minute(s) : 1 second(s)\n"

def test_minute_to_hour_days(capsys):
    minute_to_hour(1500)
    captured = capsys.readouterr()
    assert captured.out == "1 day(s) : 1 hour(s) : 0 minute(s)\n"

def test_minute_to_second(capsys):
    minute_to_second(1.5)
    captured = capsys.readouterr()
    assert captured.out == "90.0 second(s).\n"

def test_hour_to_minute(capsys):
    hour_to_minute(2)
    captured = capsys.readouterr()
    assert captured.out == "120 minute(s).\n"

def test_hour_to_second(capsys):
    hour_to_second(1.25)
    captured = capsys.readouterr()
    assert captured.out == "4500.0 second(s).\n"