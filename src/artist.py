# -*- coding: utf-8 -*-

from request import Request
from auth import Auth


class Artist(Request):
    """ Implements all the Artist methods of the API """

    def __init__(self, name=None):
        if not name:
            raise Exception("No name given")
        self.__name = name

    def addTag(self):
        pass

    def getCorrection(self):
        """ Retrieves artist corrections (canonical artist) """
        data = {'method': "artist.getcorrection",
                'artist': self.__name}
        url = self.__makeUrl__(data)
        return self.__get__(url)

    def getEvents(self):
        """ Retrieves artist events """
        data = {'method': "artist.getevents",
                'artist': self.__name}
        url = self.__makeUrl__(data)
        return self.__get__(url)

    def getInfo(self):
        """ Retrieves artist full informations """
        data = {'method': "artist.getinfo",
                'artist': self.__name}
        url = self.__makeUrl__(data)
        return self.__get__(url)

    def getPastEvents(self):
        """ Retrieves artist past events """
        data = {'method': "artist.getpastevents",
                'artist': self.__name}
        url = self.__makeUrl__(data)
        return self.__get__(url)

    def getPodcast(self):
        """ Retrieves artist podcast """
        data = {'method': "artist.getpodcast",
                'artist': self.__name}
        url = self.__makeUrl__(data)
        return self.__get__(url)

    def getShouts(self):
        """ Retrieves Artist shouts """
        data = {'method': "artist.getshouts",
                'artist': self.__name}
        url = self.__makeUrl__(data)
        return self.__get__(url)

    def getSimilar(self, limit=None):
        """ Retrieves similar Artists """
        data = {'method': "artist.getsimilar",
                'artist': self.__name}
        if limit:
            data['limit'] = limit

        url = self.__makeUrl__(data)
        return self.__get__(url)

    def getTags(self, user=None, auth=None):
        """ Retrieves Artist tags """
        data = {'method': "artist.gettags",
                'artist': self.__name}
        if user:
            data['user'] = user
        elif auth and isinstance(auth, Auth):
            
            data['api_key'] = self.API_KEY
            data['api_sig'] = auth.getSignature()
            data['sk'] = auth.getSession()
        else:
            raise Exception("Need user authentication")

        url = self.__makeUrl__(data)
        return self.__get__(url)

    def getTopAlbums(self):
        pass

    def getTopFans(self):
        pass

    def getTopTags(slef):
        pass

    def getTopTracks(self):
        pass

    def removeTag(self):
        pass

    def search(self):
        pass

    def share(self):
        pass

    def shout(self):
        pass
