# -*- coding: utf-8 -*-

from lastfm.src.chart import Chart
from lastfm.tests import Utils

from nose.tools import assert_greater
from nose.tools import assert_equal


class TestChart:
    """ Test class of Chart module """

    def __init__(self):
        self.utils = None
        self.chart = None

    def setup(self):
        self.utils = Utils()
        self.chart = Chart()

    def test_hyped_artists(self):
        """ Testing Chart hyped artists """
        chart = self.chart.get_hyped_artists()
        self.utils.assert_response_content(chart)
        assert_greater(chart['artists'], 1)

    def test_hyped_artists_with_page(self):
        """ Testing Chart hyped artists with page parameter """
        chart = self.chart.get_hyped_artists(page=2)
        self.utils.assert_response_content(chart)
        assert_equal(chart['artists']['@attr']['page'], "2")

    def test_hyped_artists_with_limit(self):
        """ Testing Chart hyped artists with limit parameter """
        chart = self.chart.get_hyped_artists(limit=1)
        self.utils.assert_response_content(chart)
        del chart['artists']['@attr']
        assert_equal(len(chart['artists']), 1)

    def test_get_hyped_tracks(self):
        """ Testing Chart hyped tracks """
        chart = self.chart.get_hyped_tracks(page=2, limit=1)
        self.utils.assert_response_content(chart)
        assert_equal(chart['tracks']['@attr']['page'], "2")
        del chart['tracks']['@attr']
        assert_equal(len(chart['tracks']), 1)

    def test_get_loved_tracks(self):
        """ Testing Chart loved tracks """
        chart = self.chart.get_loved_tracks(page=2, limit=1)
        self.utils.assert_response_content(chart)
        assert_equal(chart['tracks']['@attr']['page'], "2")
        del chart['tracks']['@attr']
        assert_equal(len(chart['tracks']), 1)

    def test_get_top_artists(self):
        """ Testing Chart top artists """
        chart = self.chart.get_top_artists(page=2, limit=1)
        self.utils.assert_response_content(chart)
        assert_equal(chart['artists']['@attr']['page'], "2")
        del chart['artists']['@attr']
        assert_equal(len(chart['artists']), 1)

    def test_get_top_tags(self):
        """ Testing Chart top tags """
        chart = self.chart.get_top_tags(page=2, limit=1)
        self.utils.assert_response_content(chart)
        assert_equal(chart['tags']['@attr']['page'], "2")
        del chart['tags']['@attr']
        assert_equal(len(chart['tags']), 1)

    def get_top_tracks(self):
        """ Testing Chart top tags """
        chart = self.chart.get_top_tracks(page=2, limit=1)
        self.utils.assert_response_content(chart)
        assert_equal(chart['tracks']['@attr']['page'], "2")
        del chart['tracks']['@attr']
        assert_equal(len(chart['tracks']), 1)
