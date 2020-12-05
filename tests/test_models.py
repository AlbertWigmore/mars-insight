""" Test API Client """
import json

import pytest

from mars_insight.models import (
    InsightMeasurement,
    InsightWeather,
)

complete_sol = '578'


def get_data():
    return json.load(open('tests/test_data/insight_data.json', 'r'))


def test_insight_weather_class():
    """Test InsightWeather class."""
    data = get_data()
    weather = InsightWeather(complete_sol, data[complete_sol])
    assert isinstance(weather, InsightWeather)


def test_insight_weather_to_json(tmp_path):
    """Test InsightWeather to_json method."""
    data = get_data()
    weather = InsightWeather(complete_sol, data[complete_sol])

    file_path = tmp_path / 'test_insight_weather_to_json.json'
    weather.to_json(file_path)

    with open(file_path, 'r') as json_fp:
        json_data = json.load(json_fp)

    assert json_data['sol'] == complete_sol
    assert json_data['data'] == data[complete_sol]


def test_insight_weather_from_json(tmp_path):
    """Test InsightWeather from_json method."""
    data = get_data()
    weather = InsightWeather(complete_sol, data[complete_sol])

    file_path = tmp_path / 'test_insight_weather_from_json.json'
    weather.to_json(file_path)

    new_weather = InsightWeather.from_json(file_path)

    assert weather.sol == new_weather.sol
    assert weather.data == new_weather.data
    assert weather.season == new_weather.season
    assert weather.first_utc == new_weather.first_utc
    assert weather.last_utc == new_weather.last_utc
    for attribute in ['unit', 'min', 'max', 'avg', 'num_measurements', 'weather_type']:
        assert getattr(weather.temperature, attribute) == getattr(new_weather.temperature, attribute)
        assert getattr(weather.wind_speed, attribute) == getattr(new_weather.wind_speed, attribute)
        assert getattr(weather.pressure, attribute) == getattr(new_weather.pressure, attribute)


def test_insight_measurement_class():
    """Test InsightMeasurement class."""
    data = get_data()
    weather = InsightMeasurement(data[complete_sol]['AT'], 'Temperature')
    assert isinstance(weather, InsightMeasurement)
