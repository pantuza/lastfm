# -*- coding: utf-8 -*-

from lastfm.src.geo import Geo
from lastfm.secrets import mysession
from lastfm.src.auth import Auth
from lastfm.tests import Utils

from nose.tools import raises
from nose.tools import assert_in
from nose.tools import assert_equal


class TestGeo:

    def __init__(self):
        self.geo = Geo()
        self.utils = None

    def setup(self):
        self.geo = Geo() 
        self.utils = Utils()


    def test_get_events(self):
        """ Testing Geo get Event """
        self.geo.get_events(location="Belo Horizonte")



#    def test_get_metro_artist_chart(self):
#    def test_get_metro_hype_artist_chart(self):
#    def test_get_metro_hype_track_chart(self):
#    def test_get_metro_track_chart(self):
#    def test_get_metro_unique_artist_chart(self):
#    def test_get_metro_unique_track_chart(self):
#    def test_get_metro_weekly_chartlist(self):
#    def test_get_metros(self):
#    def test_get_top_artists(self):
#    def test_get_top_tracks(self):

