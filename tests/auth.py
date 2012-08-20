# -*- coding: utf-8 -*-
from src.auth import Auth
from nose.tools import assert_equal
from nose.tools import assert_true
from nose.tools import raises
from selenium import webdriver

class TestAuth():

    def setup(self):
        """ Execute for every test case """
        self.auth = Auth()

    def test_get_user(self):
        """ Testing authenticated user """
        browser = webdriver.Chrome()
        browser.get(self.auth.getUserAuthUrl())
        submit = browser.find_element_by_class_name("confirmButton")
        submit.click()
        browser.close()
        self.auth.getSession()
        user = self.auth.getUser()
        assert_true(isinstance(user, basestring))

    @raises(Exception)
    def test_unauthenticated_user(self):
        """ Testing unauthenticated user """
        self.auth.getUser()

    def test_get_user_token(self):
        """ Testing the token request """
        token = self.auth.getToken()
        assert_equal(isinstance(token, basestring), True)
        assert_equal(len(token), 32)

    def test_signature_generator(self):
        """ Testing the signatureGenerator method from Auth class """
        signature = self.auth.getSignature()
        assert_equal(isinstance(signature, basestring), True)
        assert_equal(len(signature), 32)

    def test_get_user_session(self):
        """ Testing the user session request """
        session = self.auth.getSession()
        assert_true(isinstance(session, basestring))
        assert_equal(len(session), 32)
