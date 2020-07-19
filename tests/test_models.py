""" Test API Client """
import json

import pytest

from mars_insight.api import Client
from mars_insight.models import (
    InsightMeasurement,
    InsightWeather,
)

complete_sol = '578'


def get_data():
    return json.load(open('tests/test_data/insight_data.json', 'r'))


def test_insight_weather_class():
    """ Test InsightWeather class """
    data = get_data()
    weather = InsightWeather(complete_sol, data[complete_sol])
    assert isinstance(weather, InsightWeather)


def test_insight_measurement_class():
    """ Test InsightMeasurement class """
    data = get_data()
    weather = InsightMeasurement(data[complete_sol]['AT'], 'Temperature')
    assert isinstance(weather, InsightMeasurement)
