User Guide
==========

This user guide is intended to give a short overview of the library and its capabilities without delving into any details about how it is achieved. Given that the library is fairly small due to the nature of it everything should be covered here anyway.

API Client
----------

The main purpose of the `mars-insight` library is to provide a simple interface to access Mars:InSight data from the NASA API. This is can be done using the `mars_insight.api.Client` object to make requests and retrieve data. Below is an example of the different ways of calling the API which return different objects. Some of these are described in more detail in the models section.

.. code-block:: python

    from mars_insight.api import Client

    client = Client('api_key')

    # Method for retrieving raw JSON data in a dictionary.
    client.get_data()

    # Method for getting most recent weather
    # This returns a InsightWeather object.
    client.get_recent_weather()

    # Method for getting all available weather
    # This returns a list of InsightWeather object.
    client.get_weather()

Models
------

The `mars-insight` library defines objects for storing the weather data returned by the `Client` for certain methods. These are used to encapsulate the data and make it easier to read and or manipulate. The main one is the `InsightWeather` object which is responsible for storing all the available weather information for a single Sol.

.. code-block:: python

    from mars_insight.api import Client

    client = Client('api_key')

    # Method for getting most recent weather
    weather = client.get_recent_weather()

    # Print info from attributes
    print(weather.sol)
    print(weather.season)
    print(weather.first_utc)
    print(weather.last_utc)
    print(weather.temperature)
    print(weather.wind_speed)
    print(weather.pressure)

The `temperature`, `wind_speed` and `pressure` attributes are `InsightMeasurement` objects which contain attributes to get the maximum, minimum, mean, unit, number of measurements and weather type from. This can be found in the API reference.


Plotting
--------

Currently there is one function available to plot the wind `mars_insight.plot.plot_wind_rose`

.. code-block:: python

    from mars_insight.api import Client
    from mars_insight.plot import plot_wind_rose

    client = Client('api_key')

    # Method for getting most recent weather
    weather = client.get_recent_weather()

    # Plot wind rose
    plot_wind_rose(weather)
