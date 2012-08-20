# -*- coding: utf-8 -*-
from request import Request
from urllib import urlencode
import md5


class Auth(Request):
    """ Last FM authentication class """

    AUTH_URL = u"http://www.last.fm/api/auth/"
    API_SECRET = u"9435542fa196464b5306e28a0939e6f1"
    
    def __init__(self, token=None):
        if not token:
            self.__token = self.getToken()
        else:
            self.__token = token
        self.__signature = self.__signatureGenerator()

    def getUser(self):
        """ Get LAST FM authenticated user name """
        try:
            return self.__user
        except AttributeError:
            raise Exception("User not authenticated")

    def __signatureGenerator(self):
        """
        Generates the API signature based on API_KEY, user token
        and API_SECRET as defined by API documentation:

            'api_keyxxxxxxxxmethodauth.getSessiontokenxxxxxxx'
        """
        signature = u"api_key%smethodauth.getSessiontoken%s%s" % (
                    self.API_KEY, self.__token, self.API_SECRET)

        return md5.new(signature).hexdigest()

    def getToken(self):
        """ Request an user token """
        try:
            return self.__token
        except AttributeError:
            data = {'method': "auth.getToken"}
            url = self.__makeUrl__(data)
            response = self.__get__(url)
            self.__token = response['token']
            return self.__token

    def getUserAuthUrl(self):
        """ This method returns the url that your application have to 
        open it in a Browser to user give permission to the application. 
        After that, the token used in the url will be consumed by the 
        LAST FM API and you can request the user session using the 
        getSession method of the class
        """
        authUrl = "http://www.last.fm/api/auth/?"
        data = {'api_key': self.API_KEY,
                'token': self.__token}
        queryStr = urlencode(data)
        return authUrl + queryStr

    def getSession(self):
        """ Get the user session from Last FM """
        try:
            return self.__session
        except AttributeError:

            data = {'method': "auth.getSession",
                    'token': self.__token,
                    'api_sig': self.__signature}
            url = self.__makeUrl__(data)
            response = self.__get__(url)
            self.__session = response['session']['key']
            self.__user = response['session']['name']
            return self.__session

    def getSignature(self):
        """ Get the API signature """
        try:
            return self.__signature
        except AttributeError:
            self.__signature = self.__signatureGenerator()
            return self.__signature
