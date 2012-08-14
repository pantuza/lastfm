# -*- coding: utf-8 -*-
from request import Request
import md5


class Auth(Request):
    """ Last FM authentication class """

    AUTH_URL = u"http://www.last.fm/api/auth/"
    API_KEY = u"b11d3ce81059f8563bf1113af65beba5"
    API_SECRET = u"9435542fa196464b5306e28a0939e6f1"

    def __init__(self, token):
        self.__token = token
        self.__signature = self.__signatureGenerator()

    def __signatureGenerator(self):
        """
        Generates the API signature based on API_KEY, user token
        and API_SECRET as defined by API documentation:
            'api_keyxxxxxxxxmethodauth.getSessiontokenxxxxxxx'
        """
        signature = u"api_key%smethodauth.getSessiontoken%s%s" % (
                    self.API_KEY, self.__token, self.API_SECRET)

        return md5.new(signature).hexdigest()

    def getSession(self):
        """ Get the user session from Last FM """
        data = {'method': "auth.getSession",
                'token': self.__token,
                'api_key': self.API_KEY,
                'api_sig': self.__signature}
        url = self.__makeUrl__(data)

        return self.__get__(url)

    def getSignature(self):
        return self.__signature
