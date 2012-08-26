# -*- coding: utf-8 -*-

from src.artist import Artist
from src.auth import Auth
from nose.tools import assert_greater
from nose.tools import assert_true
from nose.tools import assert_in
from nose.tools import assert_not_in
from nose.tools import assert_equal
from nose.tools import raises
from secrets import mysession


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
        correction = self.artist.get_correction()
        assert_true(isinstance(correction, dict))
        assert_greater(len(correction), 0)
        self.assertErrorKey(correction)

    def test_artist_events(self):
        """ Testing Artist events """
        events = self.artist.get_events()
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assertErrorKey(events)

    def test_artist_events_with_correction(self):
        """ Testing Artist events with correction parameter """
        events = self.artist.get_events(correct=True)
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assertErrorKey(events)

    def test_artist_events_with_limit(self):
        """ Testing Artist events with limit parameter"""
        events = self.artist.get_events(limit=2)
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assertErrorKey(events)

    def test_artist_events_with_page(self):
        """ Testing Artist events with page parameter """
        events = self.artist.get_events(page=1)
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assertErrorKey(events)

    def test_artist_events_with_festivalsonly(self):
        """ Testing Artist events with festivalsonly parameter """
        events = self.artist.get_events(festivals=True)
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assertErrorKey(events)

    def test_artist_info(self):
        """ Testing Artist info """
        info = self.artist.get_info()
        assert_true(isinstance(info, dict))
        assert_greater(len(info), 0)
        self.assertErrorKey(info)

    def test_artist_past_events(self):
        """ Testing Artist past events """
        pastEvents = self.artist.get_past_events()
        assert_true(isinstance(pastEvents, dict))
        assert_greater(len(pastEvents), 0)
        self.assertErrorKey(pastEvents)

    def test_artist_podcast(self):
        """ Testing Artist podcast """
        podcast = self.artist.get_podcast()
        assert_true(isinstance(podcast, dict))
        assert_greater(len(podcast), 0)
        self.assertErrorKey(podcast)

    def test_artist_shouts(self):
        """ Testing Artist shouts """
        shouts = self.artist.get_shouts()
        assert_true(isinstance(shouts, dict))
        assert_greater(len(shouts), 0)
        self.assertErrorKey(shouts)

    def test_similar_artists(self):
        """ Testing similar artists """
        artists = self.artist.get_similar()
        assert_true(isinstance(artists, dict))
        assert_greater(len(artists), 0)
        self.assertErrorKey(artists)

    def test_similar_artists_with_limit(self):
        """ Testing similar artists with limit """
        artists = self.artist.get_similar(limit=2)
        assert_true(isinstance(artists, dict))
        assert_greater(len(artists), 0)
        self.assertErrorKey(artists)
        assert_in('similarartists', artists)
        assert_equal(len(artists['similarartists']), 2)

    def test_artist_tags(self):
        """ Testing Artist tags """
        tags = self.artist.get_tags(user='pantuza')
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assertErrorKey(tags)

    def test_artist_tags_with_no_user(self):
        """ Testing Artist tags with no user """
        auth = Auth(mysession)
        tags = self.artist.get_tags(auth=auth)
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assertErrorKey(tags)

    @raises(Exception)
    def test_artist_tag_invalid_request(self):
        """ Testing Artist tags failure """
        self.artist.get_tags()

    def test_artist_top_albums(self):
        """ Testing Artist top albums """
        albums = self.artist.get_top_albums()
        assert_true(isinstance(albums, dict))
        assert_greater(len(albums), 0)
        self.assertErrorKey(albums)

    def test_artist_top_albums_with_limit(self):
        """ Testing Artist top albums with limit parameter """
        albums = self.artist.get_top_albums(limit=2)
        assert_true(isinstance(albums, dict))
        assert_greater(len(albums), 0)
        self.assertErrorKey(albums)

    def test_artist_top_albums_with_page(self):
        """ Testing Artist top albums with page parameter """
        albums = self.artist.get_top_albums(page=2)
        assert_true(isinstance(albums, dict))
        assert_greater(len(albums), 0)
        self.assertErrorKey(albums)

    def test_artist_top_albums_with_correction(self):
        """ Testing Artist top albums with correction parameter """
        albums = self.artist.get_top_albums(correct=True)
        assert_true(isinstance(albums, dict))
        assert_greater(len(albums), 0)
        self.assertErrorKey(albums)

    def test_artist_top_fans(self):
        """ Testing Artist top fans """
        fans = self.artist.get_top_fans()
        assert_true(isinstance(fans, dict))
        assert_greater(len(fans), 0)
        self.assertErrorKey(fans)

    def test_artist_top_fans_with_correction(self):
        """ Testing Artist top fans with correction parameter """
        fans = self.artist.get_top_fans(correct=True)
        assert_true(isinstance(fans, dict))
        assert_greater(len(fans), 0)
        self.assertErrorKey(fans)

    def test_artist_top_tags(self):
        """ Testing Artist top tags """
        tags = self.artist.get_top_tags()
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assertErrorKey(tags)

    def test_artist_top_tags_with_correction(self):
        """ Testing Artist top tags with correction parameter """
        tags = self.artist.get_top_tags(correct=True)
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assertErrorKey(tags)

    def test_artist_top_tracks(self):
        """ Testing Artist top tracks """
        tracks = self.artist.get_top_tracks()
        assert_true(isinstance(tracks, dict))
        assert_greater(len(tracks), 0)
        self.assertErrorKey(tracks)

    def test_artist_top_tracks_with_limit(self):
        """ Testing Artist top tracks with limit parameter """
        tracks = self.artist.get_top_tracks(limit=3)
        assert_true(isinstance(tracks, dict))
        assert_greater(len(tracks), 0)
        self.assertErrorKey(tracks)

    def test_artist_top_tracks_with_page(self):
        """ Testing Artist top tracks with page parameter """
        tracks = self.artist.get_top_tracks(page=2)
        assert_true(isinstance(tracks, dict))
        assert_greater(len(tracks), 0)
        self.assertErrorKey(tracks)

    def test_artist_top_tracks_with_correct(self):
        """ Testing Artist top tracks with correct parameter """
        tracks = self.artist.get_top_tracks(correct=True)
        assert_true(isinstance(tracks, dict))
        assert_greater(len(tracks), 0)
        self.assertErrorKey(tracks)

    def test_artist_search(self):
        """ Testing Artist search """
        result = Artist.search(artist="the st")
        assert_true(isinstance(result, dict))
        assert_greater(len(result), 0)
        self.assertErrorKey(result)

    def test_artist_search_with_limit(self):
        """ Testing Artist search with limit parameter """
        result = Artist.search(artist="the st", limit=5)
        assert_true(isinstance(result, dict))
        assert_greater(len(result), 0)
        self.assertErrorKey(result)

    def test_artist_search_with_page(self):
        """ Testing Artist search with page parameter """
        result = Artist.search(artist="the st", page=2)
        assert_true(isinstance(result, dict))
        assert_greater(len(result), 0)
        self.assertErrorKey(result)
