# -*- coding: utf-8 -*-

from src.artist import Artist
from src.auth import Auth
from nose.tools import assert_greater
from nose.tools import assert_true
from nose.tools import assert_in
from nose.tools import assert_not_in
from nose.tools import assert_equal
from nose.tools import raises


class TestArtist():
    """ Tests the Artist class """

    def setup(self):
        self.artist = Artist("the strokes")

    def assertErrorKey(self, dictionary):
        assert_not_in("error", dictionary)

    @raises(Exception)
    def test_artist_object_exception(self):
        """ Testing Artist object creation failure """
        Artist()

    def test_artist_corrections(self):
        """ Testing Artist correction """
        correction = self.artist.getCorrection()
        assert_true(isinstance(correction, dict))
        assert_greater(len(correction), 0)
        self.assertErrorKey(correction)

    def test_artist_events(self):
        """ Testing Artist events """
        events = self.artist.getEvents()
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assertErrorKey(events)

    def test_artist_info(self):
        """ Testing Artist info """
        info = self.artist.getInfo()
        assert_true(isinstance(info, dict))
        assert_greater(len(info), 0)
        self.assertErrorKey(info)

    def test_artist_past_events(self):
        """ Testing Artist past events """
        pastEvents = self.artist.getPastEvents()
        assert_true(isinstance(pastEvents, dict))
        assert_greater(len(pastEvents), 0)
        self.assertErrorKey(pastEvents)

    def test_artist_podcast(self):
        """ Testing Artist podcast """
        podcast = self.artist.getPodcast()
        assert_true(isinstance(podcast, dict))
        assert_greater(len(podcast), 0)
        self.assertErrorKey(podcast)

    def test_artist_shouts(self):
        """ Testing Artist shouts """
        shouts = self.artist.getShouts()
        assert_true(isinstance(shouts, dict))
        assert_greater(len(shouts), 0)
        self.assertErrorKey(shouts)

    def test_similar_artists(self):
        """ Testing similar artists """
        artists = self.artist.getSimilar()
        assert_true(isinstance(artists, dict))
        assert_greater(len(artists), 0)
        self.assertErrorKey(artists)

    def test_similar_artists_with_limit(self):
        """ Testing similar artists with limit """
        artists = self.artist.getSimilar(limit=2)
        assert_true(isinstance(artists, dict))
        assert_greater(len(artists), 0)
        self.assertErrorKey(artists)
        assert_in('similarartists', artists)
        assert_equal(len(artists['similarartists']), 2)

    def test_artist_tags(self):
        """ Testing Artist tags """
        tags = self.artist.getTags(user='pantuza')
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assertErrorKey(tags)

    def test_artist_tags_with_no_user(self):
        """ Testing Artist tags with no user """
        auth = Auth("83e383ab5c81b201de7ec6f10dff75b1")
        auth.getSession()
        tags = self.artist.getTags(auth=auth)
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assertErrorKey(tags)

    @raises(Exception)
    def test_artist_tag_invalid_request(self):
        """ Testing Artist tags failure """
        self.artist.getTags()
