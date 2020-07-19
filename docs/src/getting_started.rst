User Guide
==========



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


.. code-block:: python

    from mars_weather.api import Client

    client = Client('api_key')

    data = client.get_data()


Running Tests
-------------

.. code-block:: bash

    nox