# -*- coding: utf-8 -*-
from lastfm.src.request import Request
from nose.tools import assert_equal
from nose.tools import raises


class TestRequest(Request):

    def test_get_request(self):
        """ Testing a Last FM API request """
        url = "http://ws.audioscrobbler.com/2.0/?format=json"
        response = self.__get__(url)
        assert_equal(response['error'], 3)

    @raises(Exception)
    def test_make_invalid_url(self):
        """ Testing invalid url """
        self.__makeurl__()
