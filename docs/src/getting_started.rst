Getting Started
===============

Installation
------------

Installing from PyPI.

.. code-block:: bash

    $ pip install mars-insight


Installing from source.

.. code-block bash

    $ git clone https://github.com/AlbertWigmore/mars-insight.git
    $ cd mars-insight/
    $ pip install .


Quickstart
----------

In order to use the library you will need to register for a NASA Open API key [here](https://api.nasa.gov/).

.. code-block:: python

    from mars_weather.api import Client

    client = Client('api_key')

    data = client.get_data()


Running Tests
-------------

.. code-block:: bash

    nox
