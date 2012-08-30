# -*- coding: utf-8 -*-

from nose.tools import assert_greater
from nose.tools import assert_true
from nose.tools import assert_not_in


class Utils():
    """ Utils class for tests """

    def assert_error_key(self, dictionary):  # pylint: disable=R0201
        assert_not_in("error", dictionary)

    def assert_response_content(self, dictionary):  # pylint: disable=R0201
        """ All requests responses should pass through this tests """
        assert_true(isinstance(dictionary, dict))
        assert_greater(len(dictionary), 0)
        self.assert_error_key(dictionary)
