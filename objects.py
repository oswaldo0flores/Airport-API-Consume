# HW8 - Consume API    Oswaldo Flores
"""
To handle Results.

The Results class will represent a list of results. The build url method will build
the api url (the actual building part happens in the dal module). The load method
will load in results with the given url (the actual loading data happens in the dal
module).
"""
from dal import PortsAPIBuilder, Ports
from dataclasses import dataclass, field


@dataclass
class Results:
    __results: list = field(default_factory=list)

    @staticmethod
    def build_url(ids: str, names: str, city: str, country: str, types: str, iata: str, icao: str):
        """
        To build the api url.

        To build the api url. The actual building part does not happen here. It happens
        in the dal module. This method should be static because I should not create an empty
        instance of this class to build an url.

        :param ids: A string of ids. Might be empty.
        :type ids: str
        :param names: A string of names. Might be empty.
        :type names: str
        :param city: A string of cities. Might be empty.
        :type city: str
        :param country: A string of countries. Might be empty.
        :type country: str
        :param types: A string of types. Might be empty.
        :type types: str
        :param iata: A string of iata codes. Might be empty.
        :type iata: str
        :param icao: A string of icao codes. Might be empty.
        :type icao: str
        :return:
        """
        url_builder = PortsAPIBuilder().with_end_point(PortsAPIBuilder.RESULT_END_POINT).\
            with_param(PortsAPIBuilder.ID, ids).with_param(PortsAPIBuilder.NAME, names).\
            with_param(PortsAPIBuilder.CITY, city).with_param(PortsAPIBuilder.COUNTRY, country).\
            with_param(PortsAPIBuilder.TYPE, types).with_param(PortsAPIBuilder.IATA, iata).\
            with_param(PortsAPIBuilder.ICAO, icao)
        return url_builder.build()

    @staticmethod
    def load(url: str) -> list:
        """
        To load data.

        To load data. Getting the data should happen in the dal module. This
        method should be static because I should not create an empty instance
        of this class to get data.

        :param url: An api url.
        :type url: str
        :return: A list of results. Might be empty.
        """
        return Ports().get_report(url)

