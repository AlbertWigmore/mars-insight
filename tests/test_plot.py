""" Test API Client """
import json

import pytest
import matplotlib
import matplotlib.pyplot as plt

from mars_insight.models import InsightWeather
from mars_insight.plot import plot_wind_rose

complete_sol = '578'


def get_data():
    return json.load(open('tests/test_data/insight_data.json', 'r'))


def test_plot_wind_rose():
    """Test plot_wind_rose function."""
    data = get_data()
    weather = InsightWeather(complete_sol, data[complete_sol])

    fig, axes = plot_wind_rose(weather)

    assert isinstance(fig, matplotlib.figure.Figure)
    assert isinstance(axes, matplotlib.axes.Axes)
    plt.close(fig)
