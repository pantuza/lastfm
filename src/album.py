# -*- coding: utf-8 -*-

from lastfm.src.request import Request
from lastfm.src.artist import Artist
from lastfm.src.auth import Auth


class Album(Request):

    def __init__(self, artist=None, album=None):

        if not artist or not isinstance(artist, Artist):
            raise Exception("Artist object required")
        if not album or not isinstance(album, basestring):
            raise Exception("Album parameter required")

        self.__artist = artist
        self.__album = album

    def basic_data(self, method):
        return {'method': method,
                'artist': self.__artist.get_name(),
                'album': self.__album}

    def add_tags(self, tags=None, auth=None):
        """ Add tags to an Artist album """
        if not tags:
            raise Exception("Missing tags")
        if auth and isinstance(auth, Auth):
            data = self.basic_data("album.addtags")
            data['tags'] = tags
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
        else:
            raise Exception("Missing Auth object parameter to request")
        return self.__post__(data)

    def get_buy_links(self, country=None, correct=False):
        """ Retrieve a list of buy links of an album """
        data = self.basic_data("album.getbuylinks")
        if country:
            data['country'] = country  # defined by the ISO 3166-1
        if correct:
            data['autocorrect'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_info(self, lang=None, username=None, correct=False):
        """ Retrieves album info """
        data = self.basic_data("album.getinfo")
        if username:
            data['username'] = username
        if correct:
            data['autocorrect'] = "1"
        if lang:
            data['lang'] = lang
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_shouts(self, limit=None, page=None, correct=False):
        """ Retrieves album shouts """
        data = self.basic_data("album.getshouts")
        if page:
            data['page'] = page

        if correct:
            data['autocorrect'] = "1"

        if limit:
            data['limit'] = limit
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_tags(self, user=None, auth=None, correct=False):
        """ Retrieves album tags from an user """
        data = self.basic_data("album.gettags")
        if user:
            data['user'] = user

        elif auth and isinstance(auth, Auth):
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
        else:
            raise Exception("Auth object or user name parameter required")
        if correct:
            data['autocorrect'] = "1"

        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_top_tags(self, correct=False):
        """ Retrieves the album top tags """
        data = self.basic_data("album.gettoptags")
        if correct:
            data['autocorrect'] = "1"

        url = self.__makeurl__(data)
        return self.__get__(url)

    def remove_tag(self, tag=None, auth=None):
        """ Remove an album tag """
        data = self.basic_data("album.removetag")
        if not tag:
            raise Exception("No tag given")
        data['tag'] = tag
        if auth and isinstance(auth, Auth):
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)

            return self.__post__(data)
        else:
            raise Exception("Auth object required")

    @staticmethod
    def search(album=None, limit=None, page=None):
        """ Make an album search """
        from urllib import urlopen
        from urllib import urlencode
        from json import loads

        if not album:
            raise Exception("Missing album name")
        data = {'method': "album.search",
                'album': album,
                'api_key': Request.API_KEY,
                'format': Request.REQUEST_FORMAT}
        if page:
            data['page'] = page
        if limit:
            data['limit'] = limit
        url = Request.API_URL + urlencode(data)
        return loads(urlopen(url).read())

    def share(self, recipient=None, message=None, public=False, auth=None):
        data = self.basic_data("album.share")
        if not recipient:
            raise Exception("Missing recipient ex: 'myemail@mail.com'")
        data['recipient'] = recipient
        if public:
            data['public'] = '1'
        if message:
            data['message'] = message
        if auth and isinstance(auth, Auth):
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
        else:
            raise Exception("Auth object parameter required to request")
        return self.__post__(data)
