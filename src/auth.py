# -*- coding: utf-8 -*-
from lastfm.src.request import Request
from urllib import urlencode
from hashlib import md5


class Auth(Request):
    """ Last FM authentication class """

    AUTH_URL = u"http://www.last.fm/api/auth/"
    API_SECRET = u"9435542fa196464b5306e28a0939e6f1"

    def __init__(self, session=None):
        """ Create Auth object """
        if session:
            self.__session = session
        else:
            self.__token = self.get_token()

    def sign(self, data):
        """ Generates the API signature based on API documentation """
        data['api_key'] = self.API_KEY
        keys = data.keys()
        keys.sort()
        sig_parts = [key + data[key] for key in keys]

        signature = "".join(sig_parts) + self.API_SECRET
        return md5(signature).hexdigest()

    def get_token(self):
        """ Request an user token """
        try:
            return self.__token
        except AttributeError:
            data = {'method': "auth.gettoken"}
            url = self.__makeurl__(data)
            response = self.__get__(url)
            self.__token = response['token']
            return self.__token

    def get_auth_url(self):
        """ This method returns the url that your application have to
        open it in a Browser to user give permission to the application.
        After that, the token used in the url will be consumed by the
        LAST FM API and you can request the user session using the
        get_session method of the class
        """
        auth_url = "http://www.last.fm/api/auth/?"
        data = {'api_key': self.API_KEY,
                'token': self.__token}
        query_str = urlencode(data)
        return auth_url + query_str

    def get_session(self):
        """ Get the user session from Last FM """
        try:
            return self.__session
        except AttributeError:

            data = {'method': "auth.getSession",
                    'token': self.__token}
            data['api_sig'] = self.sign(data)
            url = self.__makeurl__(data)
            response = self.__get__(url)
            self.__session = response['session']['key']
            return self.__session

    def authenticated(self):
        """ Verify if the Auth object is authenticated with Lastfm """
        return hasattr(self, '__session')
