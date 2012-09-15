# -*- coding: utf-8 -*-

from lastfm.src.request import Request
from lastfm.src.auth import Auth


class Event(Request):
    """ Implements Last FM event methods """

    ATTENDING = 0
    MAYBE_ATTENDING = 1
    NOT_ATTENDING = 2

    def __init__(self, event=None):
        if not event:
            raise Exception("Event id required")
        self.__event = unicode(event)

        self.attend_status = (self.ATTENDING,
                              self.MAYBE_ATTENDING,
                              self.NOT_ATTENDING)

    def get_event(self):
        return self.__event

    def basic_data(self, method):
        return {'method': method,
                'event': self.__event}

    def attend(self, status=None, auth=None):
        """
        Status parameter shoud be:
            (0=Attending, 1=Maybe attending, 2=Not attending)
        """
        if status not in self.attend_status:
            raise Exception("Wrong status value")
        else:
            data = self.basic_data("event.attend")
            data['status'] = unicode(status)

        if auth and isinstance(auth, Auth):
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)
        else:
            raise Exception("auth object required")
        return self.__post__(data)

    def get_attendees(self, page=None, limit=None):
        """ Retrieves event attendees """
        data = self.basic_data("event.getattendees")
        if page:
            data['page'] = page
        if limit:
            data['limit'] = limit
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_info(self):
        """ Retrieves event information """
        data = self.basic_data("event.getinfo")
        url = self.__makeurl__(data)
        return self.__get__(url)

    def get_shouts(self, page=None, limit=None):
        """ Retrieves event shouts """
        data = self.basic_data("event.getshouts")
        if page:
            data['page'] = page
        if limit:
            data['limit'] = limit

        url = self.__makeurl__(data)
        return self.__get__(url)

    def share(self, public=False, message=None, recipient=None, auth=None):
        """ share the event with recipients """
        data = self.basic_data("event.share")
        if public:
            data['public'] = "1"
        if message:
            data['message'] = message

        if not recipient:
            raise Exception("Recipient required")
        else:
            data['recipient'] = recipient
            if auth and isinstance(auth, Auth):
                data['sk'] = auth.get_session()
                data['api_sig'] = auth.sign(data)

            else:
                raise Exception("Auth object required")
        return self.__post__(data)

    def shout(self, message=None, auth=None):
        """ Post a shout on event """
        data = self.basic_data("event.shout")
        if not message:
            raise Exception("Missing message to shout")
        data['message'] = message

        if auth and isinstance(auth, Auth):
            data['sk'] = auth.get_session()
            data['api_sig'] = auth.sign(data)

        else:
            raise Exception("Auth object required")
        return self.__post__(data)
