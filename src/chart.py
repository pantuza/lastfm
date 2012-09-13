# -*- coding: utf-8 -*-

from lastfm.src.request import Request


class Chart(Request):
    """ Last FM Charts class """

    def __init__(self):
        self.__data = dict()

    def parse_params(self, page, limit):
        """ Parse functions request params """
        if page:
            self.__data['page'] = page
        if limit:
            self.__data['limit'] = limit

    def set_method(self, method):
        """ Sets the request method """
        self.__data['method'] = method

    def get_hyped_artists(self, page=None, limit=None):
        """ Retrieves the hyped artists chart """
        self.set_method("chart.gethypedartists")
        self.parse_params(page, limit)
        url = self.__makeurl__(self.__data)
        self.__data = dict()
        return self.__get__(url)

    def get_hyped_tracks(self, page=None, limit=None):
        """ Retrieves hyped tracks """
        self.set_method("chart.gethypedtracks")
        self.parse_params(page, limit)
        url = self.__makeurl__(self.__data)
        self.__data = dict()
        return self.__get__(url)

    def get_loved_tracks(self, page=None, limit=None):
        """ Retrieves loved tracks """
        self.set_method("chart.getlovedtracks")
        self.parse_params(page, limit)
        url = self.__makeurl__(self.__data)
        self.__data = dict()
        return self.__get__(url)

    def get_top_artists(self, page=None, limit=None):
        """ Retrieves top artists """
        self.set_method("chart.gettopartists")
        self.parse_params(page, limit)
        url = self.__makeurl__(self.__data)
        self.__data = dict()
        return self.__get__(url)

    def get_top_tags(self, page=None, limit=None):
        """ Retrieves top tags """
        self.set_method("chart.gettoptags")
        self.parse_params(page, limit)
        url = self.__makeurl__(self.__data)
        self.__data = dict()
        return self.__get__(url)

    def get_top_tracks(self, page=None, limit=None):
        """ Retrieves top tracks """
        self.set_method("chart.gettoptracks")
        self.parse_params(page, limit)
        url = self.__makeurl__(self.__data)
        self.__data = dict()
        return self.__get__(url)
