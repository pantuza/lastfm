# -*- coding: utf-8 -*-

from lastfm.src.request import Request
from lastfm.src.auth import Auth
from functools import wraps


class Geo(Request):
    """
        Implements Last FM Geo methods.
        Get all events in a specific location by country or city name
    """

    def __init__(self):
        self.long = None
        self.lat = None
        self.location = None
        self.distance = None
        self.page = None
        self.tag = None
        self.festivalsonly = None
        self.limit = None
        self.metro = None
        self.country = None
        self.start = None
        self.end = None

    def parse_args(func):
        """ Generic method to assign arguments to class instance """

        @wraps(func)
        def inner(self, *args, **kwargs):

            for attr in vars(self).keys():
                self.__dict__[attr] = kwargs.get(attr, None)

            return func(self, *args, **kwargs)

        return inner

    def make_data(self, method):
        """ Generic method that creates the request data dictionary """

        data = {"method": method}

        for key, value in self.__dict__.items():
            if value is not None:
                data[key] = value

        if len(data) > 1:
            return data

        raise Exception("Insufficient data provided")

    @parse_args
    def get_events(self, *args, **kwargs):
        """ Get all events in a specific location by country or city name """
        url = self.__makeurl__(self.make_data("geo.getEvents"))
        return self.__get__(url)

    @parse_args
    def get_metro_artist_chart(self, *args, **kwargs):
        """ Get a chart of artists for a metro """
        if not self.metro or not self.country:
            raise Exception("Missing metro name or country name parameters")

        url = self.__makeurl__(self.make_data("geo.getMetroArtistChart"))
        return self.__get__(url)

#    def get_metro_hype_artist_chart(self):
#    def get_metro_hype_track_chart(self):
#    def get_metro_track_chart(self):
#    def get_metro_unique_artist_chart(self):
#    def get_metro_unique_track_chart(self):
#    def get_metro_weekly_chartlist(self):
#    def get_metros(self):
#    def get_top_artists(self):
#    def get_top_tracks(self):
