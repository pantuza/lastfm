# -*- coding: utf-8 -*-
from urllib import urlopen
from urllib import urlencode
from json import loads as json_load


class Request():
    """ Last FM API request handler class """

    API_URL = "http://ws.audioscrobbler.com/2.0/?"
    REQUEST_FORMAT = "json"

    def __init__(self):
        pass

    def __get__(self, url):
        """ http GET method requests handler """
        response = urlopen(url)

        if response.code != 200:
            raise Exception("Request error :(")
        try:
            return json_load(response.read())

        except Exception as GetRequestException:
            raise GetRequestException("Error on request load")

    def __makeUrl__(self, data=None):
        """ Creates a valid url to request API """
        if not data:
            raise Exception("Invalid url params")
        data['format'] = self.REQUEST_FORMAT
        return urlencode(data)
