# -*- coding: utf-8 -*-

from src.request import Request
from src.auth import Auth


class Artist(Request):
    """ Implements all the Artist methods of the API """

    def __init__(self, name=None):
        """ Creates an Artist object """
        super(Artist, self).__init__()
        if not name:
            raise Exception("No name given")
        self.__name = name

    def add_tag(self):
        """ Add tags to artist """
        pass

    def get_correction(self):
        """ Retrieves artist corrections (canonical artist) """
        data = {'method': "artist.getcorrection",
                'artist': self.__name}
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_events(self, limit=None, page=None, correct=False, festivals=False):
        """ Retrieves artist events """
        data = {'method': "artist.getevents",
                'artist': self.__name}
        if limit:
            data['limit'] = limit
        if page:
            data['page'] = page
        if correct:
            data['autocorrect'] = "1"
        if festivals:
            data['festivalsonly'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_info(self):
        """ Retrieves artist full informations """
        data = {'method': "artist.getinfo",
                'artist': self.__name}
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_past_events(self):
        """ Retrieves artist past events """
        data = {'method': "artist.getpastevents",
                'artist': self.__name}
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_podcast(self):
        """ Retrieves artist podcast """
        data = {'method': "artist.getpodcast",
                'artist': self.__name}
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_shouts(self):
        """ Retrieves Artist shouts """
        data = {'method': "artist.getshouts",
                'artist': self.__name}
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_similar(self, limit=None):
        """ Retrieves similar Artists """
        data = {'method': "artist.getsimilar",
                'artist': self.__name}
        if limit:
            data['limit'] = limit

        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_tags(self, user=None, auth=None, correct=False):
        """ Retrieves Artist tags """
        data = {'method': "artist.gettags",
                'artist': self.__name}
        if correct:
            data['autocorrect'] = "1"
        if user:
            data['user'] = user
        elif auth and isinstance(auth, Auth):
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
        else:
            raise Exception("Need user or Auth object parameter to request")

        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_top_albums(self, limit=None, page=None, correct=False):
        """ Retrieves Artist top albums """
        data = {'method': "artist.gettopalbums",
                'artist': self.__name}
        if limit:
            data['limit'] = limit
        if page:
            data['page'] = page
        if correct:
            data['autocorrect'] = "1"

        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_top_fans(self, correct=False):
        """ Retrieve Artist top fans """
        data = {'method': "artist.gettopfans",
                'artist': self.__name}
        if correct:
            data['autocorrect'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_top_tags(self, correct=False):
        """ Retrieves Artist top Tags """
        data = {'method': "artist.gettoptags",
                'artist': self.__name}
        if correct:
            data['correct'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_top_tracks(self, limit=None, page=None, correct=False):
        """ Retrieves Artist top Tracks """
        data = {'method': "artist.gettoptracks",
                'artist': self.__name}
        if limit:
            data['limit'] = limit
        if page:
            data['page'] = page
        if correct:
            data['autocorrect'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def remove_tag(self):
        """ Remove Artist tag """
        pass

    @staticmethod
    def search(artist=None, limit=None, page=None):
        """ Static method to search for an artist """
        from urllib import urlopen
        from urllib import urlencode
        from json import loads
        if not artist:
            raise Exception("Missing artist name")
        data = {'method': "artist.search",
                'artist': artist,
                'api_key': Request.API_KEY,
                'format': Request.REQUEST_FORMAT}
        if limit:
            data['limit'] = limit
        if page:
            data['page'] = artist
        url = Request.API_URL + urlencode(data)
        return loads(urlopen(url).read())

    def share(self):
        """ Share an Artist on Lastfm """
        pass

    def shout(self):
        """ Shouts """
        pass
