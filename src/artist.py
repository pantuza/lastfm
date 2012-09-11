# -*- coding: utf-8 -*-

from lastfm.src.request import Request
from lastfm.src.auth import Auth


class Artist(Request):
    """ Implements all the Artist methods of the API """

    def __init__(self, name=None):
        """ Creates an Artist object """
        if not name:
            raise Exception("No name given")
        self.__name = name

    def get_name(self):
        return self.__name

    def basic_data(self, method):
        return {'method': method,
                'artist': self.__name}

    def add_tags(self, tags=None, auth=None):
        """ Add tags to artist """
        if tags and auth and isinstance(auth, Auth):
            data = self.basic_data("artist.addtags")
            data['tags'] = tags
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
        else:
            raise Exception("Need Auth object parameter to request")
        return self.__post__(data)

    def get_correction(self):
        """ Retrieves artist corrections (canonical artist) """
        data = self.basic_data("artist.getcorrection")
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_events(self, limit=None, page=None,
                   correct=False, festivals=False):
        """ Retrieves artist events """
        data = self.basic_data("artist.getevents")
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

    def get_info(self, lang=None, username=None, correct=False):
        """ Retrieves artist full informations """
        data = self.basic_data("artist.getinfo")
        if lang:
            data['lang'] = lang
        if username:
            data['username'] = username
        if correct:
            data['autocorrect'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_past_events(self, page=None, correct=False, limit=None):
        """ Retrieves artist past events """
        data = self.basic_data("artist.getpastevents")
        if page:
            data['page'] = page
        if correct:
            data['autocorrect'] = "1"
        if limit:
            data['limit'] = limit

        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_podcast(self, correct=False):
        """ Retrieves artist podcast """
        data = self.basic_data("artist.getpodcast")
        if correct:
            data['autocorrect'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_shouts(self, page=None, limit=None, correct=False):
        """ Retrieves Artist shouts """
        data = self.basic_data("artist.getshouts")
        if page:
            data['page'] = page
        if limit:
            data['limit'] = limit
        if correct:
            data['autocorrect'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_similar(self, limit=None):
        """ Retrieves similar Artists """
        data = self.basic_data("artist.getsimilar")
        if limit:
            data['limit'] = limit

        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_tags(self, user=None, auth=None, correct=False):
        """ Retrieves Artist tags """
        data = self.basic_data("artist.gettags")
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
        data = self.basic_data("artist.gettopalbums")
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
        data = self.basic_data("artist.gettopfans")
        if correct:
            data['autocorrect'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_top_tags(self, correct=False):
        """ Retrieves Artist top Tags """
        data = self.basic_data("artist.gettoptags")
        if correct:
            data['correct'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_top_tracks(self, limit=None, page=None, correct=False):
        """ Retrieves Artist top Tracks """
        data = self.basic_data("artist.gettoptracks")
        if limit:
            data['limit'] = limit
        if page:
            data['page'] = page
        if correct:
            data['autocorrect'] = "1"
        url = self.__makeurl__(data)
        return self.__get__(url)

    def remove_tag(self, tag=None, auth=None):
        """ Remove Artist tag """
        if tag and auth and isinstance(auth, Auth):
            data = self.basic_data("artist.removetag")
            data['tag'] = tag
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
        else:
            raise Exception("Need Auth object parameter to request")
        return self.__post__(data)

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
            data['page'] = page
        url = Request.API_URL + urlencode(data)
        return loads(urlopen(url).read())

    def share(self, recipient=None, message=None, public=False, auth=None):
        """ Share an Artist on Lastfm """
        data = self.basic_data("artist.share")
        if not recipient:
            raise Exception("Recipient required! ex: 'myemail@mail.com'")
        data['recipient'] = recipient
        if message:
            data['message'] = message
        if public:
            data['public'] = '1'
        if auth and isinstance(auth, Auth):
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
            return self.__post__(data)
        else:
            raise Exception("Need Auth object parameter to request")

    def shout(self, message=None, auth=None):
        """ Post a messagem on Artist shoutBox """
        if message and auth and isinstance(auth, Auth):
            data = self.basic_data("artist.shout")
            data['message'] = message
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
            return self.__post__(data)
        else:
            raise Exception("Missing parameters")
