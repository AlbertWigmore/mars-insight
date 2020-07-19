""" Mars Insight API Client """
import requests

URL = 'https://api.nasa.gov/insight_weather/'
FEEDTYPE = 'json'
VER = '1.0'

class Client():
    """ Client """

    def __init__(self, api_key: str):
        """ Initalise """
        self._api_key = api_key

    def weather(self):
        """ Weather """
        r = requests.get(
            URL,
            params={
                'api_key': self._api_key,
                'feedtype': FEEDTYPE,
                'ver': VER,
            },
        )

        r.raise_for_status()

        data = r.json()
        return data
