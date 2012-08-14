# -*- coding: utf-8 -*-
from src.request import Request
from nose.tools import assert_equal


class TestRequest(Request):

    def test_get_request(self):
        """ Test an Last FM API request """
        url = "http://ws.audioscrobbler.com/2.0/?format=json"
        response = self.__get__(url)
        assert_equal(response['error'], 3)
