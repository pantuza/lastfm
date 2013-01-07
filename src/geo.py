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
        self.geo_long = None
        self.geo_lat = None
        self.location = None
        self.distance = None
        self.page = None
        self.tag = None
        self.festivals = None
        self.limit = None


    def parse_args(func):

        @wraps(func)
        def inner(self, *args, **kwargs):

            for attr in vars(self).keys():
                self.__dict__[attr] = kwargs.get(attr, None)

            return func(self, *args, **kwargs)
 
        return inner

    @parse_args
    def get_events(self, *args, **kwargs):
        import ipdb
        ipdb.set_trace()
       

#    def get_metro_artist_chart(self):
#    def get_metro_hype_artist_chart(self):
#    def get_metro_hype_track_chart(self):
#    def get_metro_track_chart(self):
#    def get_metro_unique_artist_chart(self):
#    def get_metro_unique_track_chart(self):
#    def get_metro_weekly_chartlist(self):
#    def get_metros(self):
#    def get_top_artists(self):
#    def get_top_tracks(self):
