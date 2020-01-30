# -*- coding: utf-8 -*-

import pytest

from py42._internal.clients.fileevent.file_event import FileEventClient
from py42._internal.session import Py42Session

FILE_EVENT_URI = "/forensic-search/queryservice/api/v1/fileevent"
RAW_QUERY = "RAW JSON QUERY"
RAW_UNICODE_QUERY = u"RAW UNICODE JSON QUERY 我能吞"


class TestFileEventClient(object):
    @pytest.fixture
    def session(self, mocker):
        return mocker.MagicMock(spec=Py42Session)

    def test_search_file_events_calls_post_with_uri_and_query(self, session):
        client = FileEventClient(session)
        client.search_file_events(RAW_QUERY)
        session.post.assert_called_once_with(FILE_EVENT_URI, data=RAW_QUERY)

    def test_unicode_query_search_file_event_calls_post_with_query(self, session):
        client = FileEventClient(session)
        client.search_file_events(RAW_UNICODE_QUERY)
        session.post.assert_called_once_with(FILE_EVENT_URI, data=RAW_UNICODE_QUERY)
