# -*- coding: utf-8 -*-

from lastfm.src.geo import Geo
from lastfm.secrets import mysession
from lastfm.src.auth import Auth
from lastfm.tests import Utils

from nose.tools import raises
from nose.tools import assert_in
from nose.tools import assert_equal
from nose.tools import assert_greater

from datetime import datetime
from datetime import timedelta
from time import mktime


class TestGeo:

    def __init__(self):
        self.geo = Geo()
        self.utils = None

    def setup(self):
        self.geo = Geo()
        self.utils = Utils()

    @raises(Exception)
    def test_raise_data_exception(self):
        """ Testing make request data raising Exception """
        events = self.geo.get_events()

    def test_get_events_from_a_city(self):
        """ Testing Geo get Event from a city """
        events = self.geo.get_events(location="Belo Horizonte")
        self.utils.assert_response_content(events)

    def test_get_event_with_lat_and_long(self):
        """ Testing Geo get Event with latitude and longitude """
        lat = "-19.923645"
        long = "-43.919173"
        location = "Belo Horizonte"
        events = self.geo.get_events(lat=lat, long=long)
        self.utils.assert_response_content(events)
        geo = events['events']['event'][0]['venue']['location']['geo:point']
        assert_equal(geo['geo:long'], long)
        assert_equal(geo['geo:lat'], lat)

    def test_get_event_with_distance(self):
        """ Testing Geo get Event with radial distance """
        location = "London"
        distance = "300"
        events = self.geo.get_events(location=location, distance=distance)
        self.utils.assert_response_content(events)

    def test_get_event_with_page(self):
        """ Testing Geo get Event with page parameter """
        page = 2
        location = "London"
        events = self.geo.get_events(location=location, page=page)
        self.utils.assert_response_content(events)
        assert_equal(events['events']['@attr']['page'], str(page))

    def test_get_event_with_tag(self):
        """ Testing Geo get Event with tag parameter """
        location = "Belo Horizonte"
        tag = "thrash metal"
        events = self.geo.get_events(location=location, tag=tag)
        self.utils.assert_response_content(events)
        event_tag = events['events']['event'][0]['tags']['tag']
        assert_equal(event_tag, tag)

    def test_get_event_with_festivalsonly(self):
        """ Testing Geo get Event with festivalsonly parameter """
        location = "London"
        festonly = True
        events = self.geo.get_events(location=location, festivalsonly=festonly)
        self.utils.assert_response_content(events)
        assert_equal(events['events']['@attr']['festivalsonly'], "1")

    def test_get_event_with_limit(self):
        """ Testing Geo get Event with limit parameter """
        events = self.geo.get_events(location="Belo Horizonte", limit=1)
        self.utils.assert_response_content(events)
        del events['events']['@attr']
        assert_equal(len(events['events']), 1)

    def test_get_metro_artist_chart(self):
        """ Testing Geo get Metro artist """
        metro = "madrid"
        country = "spain"
        chart = self.geo.get_metro_artist_chart(metro=metro, country=country)
        self.utils.assert_response_content(chart)
        assert_greater(len(chart['topartists']['artist']), 5)

    @raises(Exception)
    def test_get_metro_artist_chart_with_no_country(self):
        """ Testing Geo get Metro artist with no country """
        self.geo.get_metro_artist_chart(metro="Baker Street")

    @raises(Exception)
    def test_get_metro_artist_chart_with_no_metro(self):
        """ Testing Geo get Metro artist with no metro name """
        self.geo.get_metro_artist_chart(country="United Kingdom")

    def test_get_metro_artist_chart_with_start(self):
        """ Testing Geo get Metro artist with start parameter """
        metro = "madrid"
        country = "spain"
        chart = self.geo.get_metro_artist_chart(metro=metro,
                                                country=country, start=5)
        self.utils.assert_response_content(chart)

    def test_get_metro_artist_chart_with_end(self):
        """ Testing Geo get Metro artist with end parameter """
        metro = "madrid"
        country = "spain"
        chart = self.geo.get_metro_artist_chart(metro=metro,
                                                country=country, end=10)
        self.utils.assert_response_content(chart)

    def test_get_metro_artist_chart_with_start_and_end(self):
        """ Testing Geo get Metro artist with start and end parameters """
        metro = "madrid"
        country = "spain"
        start = int(mktime((datetime.now() - timedelta(days=60)).timetuple()))
        end = int(mktime(datetime.now().timetuple()))
        chart = self.geo.get_metro_artist_chart(metro=metro, country=country,
                                                start=start, end=end)
        self.utils.assert_response_content(chart)

    def test_get_metro_artist_chart_with_page(self):
        """ Testing Geo get Metro artist with page parameter """
        metro = "madrid"
        country = "spain"
        page = '2'
        chart = self.geo.get_metro_artist_chart(metro=metro,
                                                country=country, page=page)
        self.utils.assert_response_content(chart)
        assert_equal(chart['topartists']['@attr']['page'], page)

    def test_get_metro_artist_chart_with_limit(self):
        """ Testing Geo get Metro artist with limit parameter """
        metro = "madrid"
        country = "spain"
        limit = '1'
        chart = self.geo.get_metro_artist_chart(metro=metro,
                                                country=country, limit=limit)
        self.utils.assert_response_content(chart)
        import ipdb
        ipdb.set_trace()
        assert_equal(chart['topartists']['@attr']['perPage'], limit)
        del chart['topartists']['@attr']
        assert_equal(len(chart['topartists']), int(limit))

#    def test_get_metro_hype_artist_chart(self):
#    def test_get_metro_hype_track_chart(self):
#    def test_get_metro_track_chart(self):
#    def test_get_metro_unique_artist_chart(self):
#    def test_get_metro_unique_track_chart(self):
#    def test_get_metro_weekly_chartlist(self):
#    def test_get_metros(self):
#    def test_get_top_artists(self):
#    def test_get_top_tracks(self):
