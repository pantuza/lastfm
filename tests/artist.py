# -*- coding: utf-8 -*-

from lastfm.src.artist import Artist
from lastfm.src.auth import Auth
from nose.tools import assert_greater
from nose.tools import assert_true
from nose.tools import assert_in
from nose.tools import assert_not_in
from nose.tools import assert_equal
from nose.tools import raises
from lastfm.secrets import mysession


class TestArtist():
    """ Tests the Artist class """

    def __init__(self):
        self.artist = None

    def setup(self):
        self.artist = Artist("the strokes")
    
    @classmethod
    def assert_error_key(cls, dictionary):
        assert_not_in("error", dictionary)
    
    @classmethod
    @raises(Exception)
    def test_object_exception(cls):
        """ Testing Artist object creation failure """
        Artist()

    def test_corrections(self):
        """ Testing Artist correction """
        correction = self.artist.get_correction()
        assert_true(isinstance(correction, dict))
        assert_greater(len(correction), 0)
        self.assert_error_key(correction)

    def test_artist_events(self):
        """ Testing Artist events """
        events = self.artist.get_events()
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assert_error_key(events)

    def test_events_correction(self):
        """ Testing Artist events with correction parameter """
        events = self.artist.get_events(correct=True)
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assert_error_key(events)

    def test_events_limit(self):
        """ Testing Artist events with limit parameter"""
        events = self.artist.get_events(limit=2)
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assert_error_key(events)

    def test_events_page(self):
        """ Testing Artist events with page parameter """
        events = self.artist.get_events(page=1)
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assert_error_key(events)

    def test_events_festivalsonly(self):
        """ Testing Artist events with festivalsonly parameter """
        events = self.artist.get_events(festivals=True)
        assert_true(isinstance(events, dict))
        assert_greater(len(events), 0)
        self.assert_error_key(events)

    def test_info(self):
        """ Testing Artist info """
        info = self.artist.get_info()
        assert_true(isinstance(info, dict))
        assert_greater(len(info), 0)
        self.assert_error_key(info)

    def test_past_events(self):
        """ Testing Artist past events """
        past_events = self.artist.get_past_events()
        assert_true(isinstance(past_events, dict))
        assert_greater(len(past_events), 0)
        self.assert_error_key(past_events)

    def test_podcast(self):
        """ Testing Artist podcast """
        podcast = self.artist.get_podcast()
        assert_true(isinstance(podcast, dict))
        assert_greater(len(podcast), 0)
        self.assert_error_key(podcast)

    def test_shouts(self):
        """ Testing Artist shouts """
        shouts = self.artist.get_shouts()
        assert_true(isinstance(shouts, dict))
        assert_greater(len(shouts), 0)
        self.assert_error_key(shouts)

    def test_similar_artists(self):
        """ Testing similar artists """
        artists = self.artist.get_similar()
        assert_true(isinstance(artists, dict))
        assert_greater(len(artists), 0)
        self.assert_error_key(artists)

    def test_similar_artists_limit(self):
        """ Testing similar artists with limit """
        artists = self.artist.get_similar(limit=2)
        assert_true(isinstance(artists, dict))
        assert_greater(len(artists), 0)
        self.assert_error_key(artists)
        assert_in('similarartists', artists)
        assert_equal(len(artists['similarartists']), 2)

    def test_tags(self):
        """ Testing Artist tags """
        tags = self.artist.get_tags(user='pantuza')
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assert_error_key(tags)

    def test_tags_no_user(self):
        """ Testing Artist tags with no user """
        auth = Auth(mysession)
        tags = self.artist.get_tags(auth=auth)
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assert_error_key(tags)

    @raises(Exception)
    def test_tag_invalid_request(self):
        """ Testing Artist tags failure """
        self.artist.get_tags()

    def test_top_albums(self):
        """ Testing Artist top albums """
        albums = self.artist.get_top_albums()
        assert_true(isinstance(albums, dict))
        assert_greater(len(albums), 0)
        self.assert_error_key(albums)

    def test_top_albums_limit(self):
        """ Testing Artist top albums with limit parameter """
        albums = self.artist.get_top_albums(limit=2)
        assert_true(isinstance(albums, dict))
        assert_greater(len(albums), 0)
        self.assert_error_key(albums)

    def test_top_albums_page(self):
        """ Testing Artist top albums with page parameter """
        albums = self.artist.get_top_albums(page=2)
        assert_true(isinstance(albums, dict))
        assert_greater(len(albums), 0)
        self.assert_error_key(albums)

    def test_top_albums_correction(self):
        """ Testing Artist top albums with correction parameter """
        albums = self.artist.get_top_albums(correct=True)
        assert_true(isinstance(albums, dict))
        assert_greater(len(albums), 0)
        self.assert_error_key(albums)

    def test_top_fans(self):
        """ Testing Artist top fans """
        fans = self.artist.get_top_fans()
        assert_true(isinstance(fans, dict))
        assert_greater(len(fans), 0)
        self.assert_error_key(fans)

    def test_top_fans_correction(self):
        """ Testing Artist top fans with correction parameter """
        fans = self.artist.get_top_fans(correct=True)
        assert_true(isinstance(fans, dict))
        assert_greater(len(fans), 0)
        self.assert_error_key(fans)

    def test_top_tags(self):
        """ Testing Artist top tags """
        tags = self.artist.get_top_tags()
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assert_error_key(tags)

    def test_top_tags_correction(self):
        """ Testing Artist top tags with correction parameter """
        tags = self.artist.get_top_tags(correct=True)
        assert_true(isinstance(tags, dict))
        assert_greater(len(tags), 0)
        self.assert_error_key(tags)

    def test_top_tracks(self):
        """ Testing Artist top tracks """
        tracks = self.artist.get_top_tracks()
        assert_true(isinstance(tracks, dict))
        assert_greater(len(tracks), 0)
        self.assert_error_key(tracks)

    def test_top_tracks_limit(self):
        """ Testing Artist top tracks with limit parameter """
        tracks = self.artist.get_top_tracks(limit=3)
        assert_true(isinstance(tracks, dict))
        assert_greater(len(tracks), 0)
        self.assert_error_key(tracks)

    def test_top_tracks_page(self):
        """ Testing Artist top tracks with page parameter """
        tracks = self.artist.get_top_tracks(page=2)
        assert_true(isinstance(tracks, dict))
        assert_greater(len(tracks), 0)
        self.assert_error_key(tracks)

    def test_top_tracks_correct(self):
        """ Testing Artist top tracks with correct parameter """
        tracks = self.artist.get_top_tracks(correct=True)
        assert_true(isinstance(tracks, dict))
        assert_greater(len(tracks), 0)
        self.assert_error_key(tracks)

    def test_search(self):
        """ Testing Artist search """
        result = Artist.search(artist="the st")
        assert_true(isinstance(result, dict))
        assert_greater(len(result), 0)
        self.assert_error_key(result)

    def test_search_limit(self):
        """ Testing Artist search with limit parameter """
        result = Artist.search(artist="the st", limit=5)
        assert_true(isinstance(result, dict))
        assert_greater(len(result), 0)
        self.assert_error_key(result)

    def test_search_page(self):
        """ Testing Artist search with page parameter """
        result = Artist.search(artist="the st", page=2)
        assert_true(isinstance(result, dict))
        assert_greater(len(result), 0)
        self.assert_error_key(result)
