# -*- coding: utf-8 -*-
from urllib import urlopen
from urllib import urlencode
from json import loads as json_load


class Request(object):
    """ Last FM API request handler class """

    API_KEY = u"b11d3ce81059f8563bf1113af65beba5"
    API_URL = "http://ws.audioscrobbler.com/2.0/?"
    REQUEST_FORMAT = "json"

    def __init__(self):
        self.__response = None

    def __get__(self, url):
        """ http GET request method handler """
        self.__response = urlopen(url)

        if self.__ok__():
            return json_load(self.__response.read())
        else:
            raise Exception("Request error :(")

    def __post__(self, data):
        """ Http POST request method handler """
        data['api_key'] = self.API_KEY
        data['format'] = self.REQUEST_FORMAT
        self.__response = urlopen(self.API_URL, urlencode(data))

        if self.__ok__():
            return json_load(self.__response.read())
        else:
            raise Exception("Request error :(")

    def __makeurl__(self, data=None):
        """ Creates a valid url to request API """
        if not data:
            raise Exception("Invalid url params")
        data['format'] = self.REQUEST_FORMAT
        data['api_key'] = self.API_KEY
        return self.API_URL + urlencode(data)

    def __ok__(self):
        """ Verify request success """
        return self.__response.code == 200
