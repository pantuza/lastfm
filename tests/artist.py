# -*- coding: utf-8 -*-

from lastfm.src.artist import Artist
from lastfm.src.auth import Auth
from lastfm.tests import Utils
from nose.tools import assert_in
from nose.tools import assert_equal
from nose.tools import raises
from lastfm.secrets import mysession


class TestArtist():
    """ Tests the Artist class """

    def __init__(self):
        self.artist = None
        self.utils = None

    def setup(self):
        self.artist = Artist("the strokes")
        self.utils = Utils()

    @raises(Exception)
    def test_object_exception(self):
        """ Testing Artist object creation failure """
        self.artist = Artist()

    def test_add_tags(self):
        """ Testing Artist add tags """
        tag = u'test api'
        auth = Auth(mysession)
        tags = self.artist.add_tags(tags=tag, auth=auth)
        self.utils.assert_response_content(tags)
        assert_equal(tags['status'], 'ok')
        tags = self.artist.get_tags(auth=auth)
        assert_equal(tags['tags']['tag']['name'], tag)

    @raises(Exception)
    def test_add_tag_with_no_auth(self):
        """ Testing Artist add tag with no auth parameter """
        self.artist.get_tags(tags='test api')

    def test_corrections(self):
        """ Testing Artist correction """
        correction = self.artist.get_correction()
        self.utils.assert_response_content(correction)

    def test_events(self):
        """ Testing Artist events """
        events = self.artist.get_events()
        self.utils.assert_response_content(events)

    def test_events_correction(self):
        """ Testing Artist events with correction parameter """
        events = self.artist.get_events(correct=True)
        self.utils.assert_response_content(events)

    def test_events_limit(self):
        """ Testing Artist events with limit parameter"""
        events = self.artist.get_events(limit=2)
        self.utils.assert_response_content(events)

    def test_events_page(self):
        """ Testing Artist events with page parameter """
        events = self.artist.get_events(page=1)
        self.utils.assert_response_content(events)

    def test_events_festivalsonly(self):
        """ Testing Artist events with festivalsonly parameter """
        events = self.artist.get_events(festivals=True)
        self.utils.assert_response_content(events)

    def test_info(self):
        """ Testing Artist info """
        info = self.artist.get_info()
        self.utils.assert_response_content(info)

    def test_info_lang(self):
        """ Testing Artist info with lang parameter """
        # portuguese language in ISO 639 alpha-2 code
        info = self.artist.get_info(lang='por')
        self.utils.assert_response_content(info)
        # there is no Artist biography in portuguese
        assert_equal(len(info['artist']['bio']['content']), 0)

    def test_info_autocorrect(self):
        """ Testing Artist info with correction """
        self.artist = Artist("the stroke")
        info = self.artist.get_info(correct=True)
        self.utils.assert_response_content(info)
        assert_equal(info['artist']['name'], u"The Strokes")

    def test_info_username(self):
        """ Testing Artist info with username parameter """
        info = self.artist.get_info(username="pantuza")
        self.utils.assert_response_content(info)
        assert_in('userplaycount', info['artist']['stats'])

    def test_past_events(self):
        """ Testing Artist past events """
        past_events = self.artist.get_past_events()
        self.utils.assert_response_content(past_events)
        assert_in('event', past_events['events'])

    def test_past_events_page(self):
        """ Testing Artist past events with page parameter """
        past_events = self.artist.get_past_events(page=2)
        self.utils.assert_response_content(past_events)
        assert_in('event', past_events['events'])

    def test_past_events_correct(self):
        """ Testing Artist past event with correct parameter """
        self.artist = Artist("the stroke")
        past_events = self.artist.get_past_events(correct=True)
        self.utils.assert_response_content(past_events)
        assert_in(u"The Strokes", past_events['events']['@attr']['artist'])

    def test_past_events_limit(self):
        """ Testing Artist past event with limit parameter """
        past_events = self.artist.get_past_events(limit=1)
        self.utils.assert_response_content(past_events)
        del past_events['events']['@attr']
        assert_equal(len(past_events), 1)

    def test_podcast(self):
        """ Testing Artist podcast """
        podcast = self.artist.get_podcast()
        self.utils.assert_response_content(podcast)

    def test_podcast_correct(self):
        """ Testing Artist podcast with correct parameter """
        self.artist = Artist('The stroke')
        podcast = self.artist.get_podcast(correct=True)
        self.utils.assert_response_content(podcast)

    def test_shouts(self):
        """ Testing Artist shouts """
        shouts = self.artist.get_shouts()
        self.utils.assert_response_content(shouts)

    def test_shouts_limit(self):
        """ Testing Artist shouts with limit parameter """
        shouts = self.artist.get_shouts(limit=1)
        self.utils.assert_response_content(shouts)
        del shouts['shouts']['@attr']
        assert_equal(len(shouts['shouts']), 1)

    def test_shouts_page(self):
        """ Testing Artist shouts with page parameter """
        shouts = self.artist.get_shouts(page=2)
        self.utils.assert_response_content(shouts)
        assert_equal(shouts['shouts']['@attr']['page'], "2")

    def test_shouts_correct(self):
        """ Testing Artist shouts with correct parameter """
        self.artist = Artist("the stroke")
        shouts = self.artist.get_shouts(correct=True)
        self.utils.assert_response_content(shouts)
        assert_equal(u"The Strokes", shouts['shouts']['@attr']['artist'])

    def test_similar_artists(self):
        """ Testing similar artists """
        artists = self.artist.get_similar()
        self.utils.assert_response_content(artists)

    def test_similar_artists_limit(self):
        """ Testing similar artists with limit """
        artists = self.artist.get_similar(limit=2)
        self.utils.assert_response_content(artists)
        assert_in('similarartists', artists)
        assert_equal(len(artists['similarartists']), 2)

    def test_tags(self):
        """ Testing Artist tags """
        tags = self.artist.get_tags(user='pantuza')
        self.utils.assert_response_content(tags)

    def test_tags_no_user(self):
        """ Testing Artist tags with no user """
        auth = Auth(mysession)
        tags = self.artist.get_tags(auth=auth)
        self.utils.assert_response_content(tags)

    @raises(Exception)
    def test_tag_invalid_request(self):
        """ Testing Artist tags failure """
        self.artist.get_tags()

    def test_top_albums(self):
        """ Testing Artist top albums """
        albums = self.artist.get_top_albums()
        self.utils.assert_response_content(albums)

    def test_top_albums_limit(self):
        """ Testing Artist top albums with limit parameter """
        albums = self.artist.get_top_albums(limit=2)
        self.utils.assert_response_content(albums)

    def test_top_albums_page(self):
        """ Testing Artist top albums with page parameter """
        albums = self.artist.get_top_albums(page=2)
        self.utils.assert_response_content(albums)

    def test_top_albums_correction(self):
        """ Testing Artist top albums with correction parameter """
        albums = self.artist.get_top_albums(correct=True)
        self.utils.assert_response_content(albums)

    def test_top_fans(self):
        """ Testing Artist top fans """
        fans = self.artist.get_top_fans()
        self.utils.assert_response_content(fans)

    def test_top_fans_correction(self):
        """ Testing Artist top fans with correction parameter """
        fans = self.artist.get_top_fans(correct=True)
        self.utils.assert_response_content(fans)

    def test_top_tags(self):
        """ Testing Artist top tags """
        tags = self.artist.get_top_tags()
        self.utils.assert_response_content(tags)

    def test_top_tags_correction(self):
        """ Testing Artist top tags with correction parameter """
        tags = self.artist.get_top_tags(correct=True)
        self.utils.assert_response_content(tags)

    def test_top_tracks(self):
        """ Testing Artist top tracks """
        tracks = self.artist.get_top_tracks()
        self.utils.assert_response_content(tracks)

    def test_top_tracks_limit(self):
        """ Testing Artist top tracks with limit parameter """
        tracks = self.artist.get_top_tracks(limit=3)
        self.utils.assert_response_content(tracks)

    def test_top_tracks_page(self):
        """ Testing Artist top tracks with page parameter """
        tracks = self.artist.get_top_tracks(page=2)
        self.utils.assert_response_content(tracks)

    def test_top_tracks_correct(self):
        """ Testing Artist top tracks with correct parameter """
        tracks = self.artist.get_top_tracks(correct=True)
        self.utils.assert_response_content(tracks)

    def test_remove_tags(self):
        """ Testing Artist add tags """
        tag = u'test api'
        auth = Auth(mysession)
        tags = self.artist.remove_tag(tag=tag, auth=auth)
        self.utils.assert_response_content(tags)
        assert_equal(tags['status'], 'ok')

    def test_search(self):
        """ Testing Artist search """
        result = Artist.search(artist="the st")
        self.utils.assert_response_content(result)

    def test_search_limit(self):
        """ Testing Artist search with limit parameter """
        result = Artist.search(artist="the st", limit=5)
        self.utils.assert_response_content(result)

    def test_search_page(self):
        """ Testing Artist search with page parameter """
        result = Artist.search(artist="the st", page=2)
        self.utils.assert_response_content(result)

    def test_artist_share(self):
        """ Testing Artist share """
        auth = Auth(mysession)
        share = self.artist.share(recipient="lastfm", message="api test",
                                  public=True, auth=auth)

        self.utils.assert_response_content(share)
        assert_equal(share['status'], 'ok')

    @raises(Exception)
    def test_exception_on_shout(self):
        """ Testing Artist shout with no message """
        self.artist.shout()

    def test_post_shout(self):
        """ Testing Artist shout """
        auth = Auth(mysession)
        shout = self.artist.shout(message="nice Indie rock band", auth=auth)
        self.utils.assert_response_content(shout)
        assert_equal(shout['status'], 'ok')
