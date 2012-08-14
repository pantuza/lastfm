# -*- coding: utf-8 -*-
from src.auth import Auth
from nose.tools import assert_equal


class TestAuth():

    FAKE_TOKEN = "e176d5570d54fb7e9e101c6235acf944"

    def test_signature_generator(self):
        """ Testing the signatureGenerator method from Auth class """
        auth = Auth(self.FAKE_TOKEN)
        assert_equal(auth.getSignature(), "00a2b38cdee449117c9b21c16430c5d5")

    def test_get_user_session(self):

