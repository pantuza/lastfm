# -*- coding: utf-8 -*-

from lastfm.src.event import Event
from lastfm.secrets import mysession
from lastfm.src.auth import Auth
from lastfm.tests import Utils

from nose.tools import raises
from nose.tools import assert_in
from nose.tools import assert_equal


class TestEvent:

    def __init__(self):
        self.event = None
        self.utils = None

    def setup(self):
        self.event = Event(3388376)
        self.utils = Utils()

    def test_attend(self):
        """ Testing Event attend """
        auth = Auth(mysession)
        event = self.event.attend(status=Event.ATTENDING, auth=auth)
        self.utils.assert_response_content(event)

    @raises(Exception)
    def test_attend_with_no_status(self):
        """ Testing Event attend with no status parameter """
        self.event.attend()

    @raises(Exception)
    def test_attend_with_invalid_status(self):
        """ Testing Event attend with invalid status """
        self.event.attend(status=3)

    @raises(Exception)
    def test_attend_with_no_auth(self):
        """ Testing Event attend with no auth object """
        self.event.attend(status=Event.ATTENDING)

    def test_get_attendees(self):
        """ Testing Event get attendees """
        attendees = self.event.get_attendees(page=0, limit=1)
        self.utils.assert_response_content(attendees)
        assert_equal(attendees['attendees']['@attr']['page'], "1")
        del attendees['attendees']['@attr']
        assert_equal(len(attendees['attendees']), 1)

    def test_get_info(self):
        """ Testing Event get info """
        event = self.event.get_info()
        self.utils.assert_response_content(event)
        assert_equal(event['event']['id'], unicode(self.event.get_event()))

    def test_get_shouts(self):
        """ Testing Event get shouts """
        shouts = self.event.get_shouts()
        self.utils.assert_response_content(shouts)
        assert_in("shouts", shouts)

    def test_share(self):
        """ Testing Event share """
        auth = Auth(mysession)
        message = "testing api event share"
        share = self.event.share(public=False, message=message,
                                 recipient="lastfm", auth=auth)
        self.utils.assert_response_content(share)

    @raises(Exception)
    def test_share_with_no_auth(self):
        """ Testing Event share with no auth """
        self.event.share(recipient="lastfm")

    def test_shout(self):
        """ Testing Event shout """
        auth = Auth(mysession)
        message = "More one api test"
        shout = self.event.shout(message=message, auth=auth)
        self.utils.assert_response_content(shout)

    @raises(Exception)
    def test_shout_with_no_message(self):
        """ Testing Event shout with no message """
        self.event.shout()

    @raises(Exception)
    def test_shout_with_no_auth(self):
        """ Testing Event Shout with no auth """
        message = "api test"
        self.event.shout(message=message)
