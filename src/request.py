# -*- coding: utf-8 -*-
from urllib import urlopen
from urllib import urlencode
from json import loads as json_load


class Request(object):
    """ Last FM API request handler class """

    API_KEY = u"b11d3ce81059f8563bf1113af65beba5"
    API_URL = "http://ws.audioscrobbler.com/2.0/?"
    REQUEST_FORMAT = "json"

    def __get__(self, url):
        """ http GET method requests handler """
        response = urlopen(url)

        if response.code != 200:
            raise Exception("Request error :(")

        return json_load(response.read())

    def __makeurl__(self, data=None):
        """ Creates a valid url to request API """
        if not data:
            raise Exception("Invalid url params")
        data['format'] = self.REQUEST_FORMAT
        data['api_key'] = self.API_KEY
        return self.API_URL + urlencode(data)
