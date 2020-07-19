""" Test API Client """
import os

import pytest

from mars_insight.api import Client
from mars_insight.models import (
    InsightMeasurement,
    InsightWeather,
)

API_KEY = os.environ['INSIGHT_API_KEY']


def test_client_class():
    """ Test object creation """
    client = Client(API_KEY)
    assert isinstance(client, Client)


def test_client_get_data():
    """ Test Client get_data method """
    client = Client(API_KEY)
    data = client.get_data()
    assert data


def test_client_get_recent_weather():
    """ Test Client get_recent_weather method """
    client = Client(API_KEY)
    weather = client.get_recent_weather()
    assert isinstance(weather, InsightWeather)


def test_client_get_weather():
    """ Test Client get_weather method """
    client = Client(API_KEY)
    weather_list = client.get_weather()
    for weather in weather_list:
        assert isinstance(weather, InsightWeather)
