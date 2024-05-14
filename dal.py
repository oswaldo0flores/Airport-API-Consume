# HW8 - Consume API    Oswaldo Flores
"""
To handle apis and the creation of an url.

The APIBuilder class represent the creation of an url. The with param method
represents the parameters of an url. The build method will build the url.
The PortsAPIBuilder class represent the creation of an url for ports. The init
method should initialize the class with a base url. The with end point will get
the end point of an url. The with param represents the parameters of an url.
The Ports class represent an API call for ports. The get reports method will
make an API call with a given url.

ID: A key value for id.
NAME: A key value for name.
CITY: A key value for city.
COUNTRY: A key value for country.
TYPE: A key value for type.
IATA: A key value for iata.
ICAO: A key value for icao.
RESULT_END_POINT: The end point of an url.
OK_CODE: The api call was successful.
"""
from abc import ABC, abstractmethod
import requests


class APIBuilder(ABC):
    def __init__(self, base_url):
        """
        To initialize the class.

        To initialize the class. The class will get initialize with a given base
        url.

        :param base_url: The first part of an url.
        """
        self._base_url = base_url
        self._end_point = ''
        self._params = {}

    @abstractmethod
    def with_param(self, param_name, param_value):
        """
        To form the parameter part of the url.

        To form the parameter part if the url.

        :param param_name: The key for the value.
        :param param_value: The value for the key.
        """
        pass

    def build(self):
        """
        To build the url.

        To build the url with this class private fields. This
        method should not validate if the url works.

        :return: The api url.
        """
        query_string = f'{self._base_url}{self._end_point}'
        if len(self._params) == 0:
            return query_string
        else:
            query_string = f'{query_string}?'
            param_string = '&'.join([f'{k}={v}' for k, v in self._params.items()])
            return f'{query_string}{param_string}'


class PortsAPIBuilder(APIBuilder):
    ID = 'id'
    NAME = 'name'
    CITY = 'city'
    COUNTRY = 'country'
    TYPE = 'type'
    IATA = 'iata'
    ICAO = 'icao'
    RESULT_END_POINT = '/results/'

    def __init__(self):
        """
        To initialize the class.

        To initialize the class using the base constructor.
        """
        super().__init__('http://localhost/HW8')

    def with_end_point(self, end_point):
        """
        To set the base class private field of end point.

        To set the base class private field of end point.

        :param end_point: End part of the url.
        :return: Itself.
        """
        self._end_point = end_point
        return self

    def with_param(self, param_name, param_value):
        """
        To set the parameters.

        To set the parameters. If the give param value is empty just return itself.

        :param param_name: The key for the value.
        :param param_value: The value(parameters) for the key.
        :return: Itself.
        """
        if param_value != '':
            self._params[param_name] = param_value
            return self
        return self


class Ports:
    OK_CODE = 200

    def get_report(self, request_url):
        """
        To get a list of reports.

        To make an api call with the given url. It is okay if I got nothing
        from the api call. It is okay if I encounter an error.

        :param request_url: The full url to make an api call.
        :return: None if an error occurs. A list of ports if no error occurs.
        """
        try:
            while True:
                response = requests.get(request_url)
                if response.status_code == self.OK_CODE:
                    ports = response.json()
                    return ports
                else:
                    response.raise_for_status()
        except requests.exceptions.RequestException as err:
            return None

