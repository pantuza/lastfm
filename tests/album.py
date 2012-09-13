# -*- coding: utf-8 -*-

from lastfm.src.album import Album
from lastfm.src.artist import Artist
from lastfm.src.auth import Auth
from lastfm.tests import Utils
from lastfm.secrets import mysession

from nose.tools import raises
from nose.tools import assert_greater
from nose.tools import assert_in
from nose.tools import assert_equal


class TestAlbum:

    def __init__(self):
        self.artist = None
        self.auth = None
        self.album = None
        self.utils = None

    def setup(self):

        self.artist = Artist("Foo fighters")
        self.auth = Auth(mysession)
        self.album = Album(artist=self.artist, album="Wasting Light")
        self.utils = Utils()

    @raises(Exception)
    def test_album_with_no_artist(self):
        """ Testing Album with no artist """
        self.album = Album(album="Wasting Light")

    @raises(Exception)
    def test_album_with_no_album(self):
        """ Testing Album with no album name """
        self.album = Album(artist=self.artist)

    def test_add_tags(self):
        """ Testing Album add tags  """
        tags = self.album.add_tags(tags="api test", auth=self.auth)
        self.utils.assert_response_content(tags)

    @raises(Exception)
    def test_add_tags_with_no_auth(self):
        """ Testing Album add tags with no auth object """
        self.album.add_tags(tags="api test")

    def test_get_buy_links(self):
        """ Testing Album buy links """
        buy_links = self.album.get_buy_links(country="Brazil", correct=True)
        self.utils.assert_response_content(buy_links)
        assert_greater(buy_links['affiliations'], 0)

    def test_get_info(self):
        """ Testing Album information """
        info = self.album.get_info()
        self.utils.assert_response_content(info)
        assert_in("name", info['album'])

    def test_get_info_with_username(self):
        """ Testing Album information with username parameter """
        info = self.album.get_info(username="pantuza")
        self.utils.assert_response_content(info)
        assert_in('userplaycount', info['album'])

    def test_get_info_with_lang(self):
        """ Testing Album information with language parameter """
        info = self.album.get_info(lang="por")
        self.utils.assert_response_content(info)

    def test_get_shouts(self):
        """ Testing Album shouts """
        shouts = self.album.get_shouts()
        self.utils.assert_response_content(shouts)

    def test_get_shouts_with_limit(self):
        """ Testing Album shouts with limit parameter """
        shouts = self.album.get_shouts(limit=1)
        self.utils.assert_response_content(shouts)
        del shouts['shouts']['@attr']
        assert_equal(len(shouts['shouts']), 1)

    def test_get_shouts_with_page(self):
        """ Testing Album shouts with page parameter """
        shouts = self.album.get_shouts(page=2)
        self.utils.assert_response_content(shouts)
        assert_equal(shouts['shouts']['@attr']['page'], '2')

    def test_get_tags(self):
        """ Testing Album tags """
        auth = Auth(mysession)
        tags = self.album.get_tags(auth=auth)
        self.utils.assert_response_content(tags)
        assert_in("name", tags['tags']['tag'])

    def test_get_tags_with_user(self):
        """ Testing Album tags with username """
        tags = self.album.get_tags(user="pantuza")
        self.utils.assert_response_content(tags)
        del tags['tags']['@attr']
        assert_equal(len(tags['tags']), 1)

    def test_get_top_tags(self):
        """ Testing Album top tags """
        tags = self.album.get_top_tags(correct=True)
        self.utils.assert_response_content(tags)
        assert_in("name", tags['toptags']['tag'][0])

    def test_remove_tag(self):
        """ Testing Album remove tag """
        auth = Auth(mysession)
        tag = self.album.remove_tag(tag="api test", auth=auth)
        self.utils.assert_response_content(tag)

    def test_search(self):
        """ Testing Album search """
        result = Album.search(album="the st")
        self.utils.assert_response_content(result)

    def test_search_limit(self):
        """ Testing Album search with limit parameter """
        result = Album.search(album="the st", limit=5)
        self.utils.assert_response_content(result)

    def test_search_page(self):
        """ Testing Album search with page parameter """
        result = Album.search(album="the st", page=2)
        self.utils.assert_response_content(result)

    def test_share(self):
        """ Testing Album share """
        auth = Auth(mysession)
        share = self.album.share(recipient="lastfm", message="api test",
                                 public=True, auth=auth)

        self.utils.assert_response_content(share)
        assert_equal(share['status'], 'ok')

    @raises(Exception)
    def test_share_with_no_auth(self):
        """ Testing Album share with no auth object """
        self.album.share(recipient="lastfm", message="api test",
                         public=True)

    @raises(Exception)
    def test_share_with_no_recipient(self):
        """ Testing Album share with no recipient """
        self.album.share(message="api test", public=True)
