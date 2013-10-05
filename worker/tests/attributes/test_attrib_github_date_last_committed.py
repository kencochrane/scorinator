import datetime

from attributes.attrib_github_date_last_committed import (run, score, WEIGHT,
                                                          ATTRIBUTE_SLUG)
from mock import Mock, patch

class TestAttribGitHubDateLastCommittedRun(object):
    def test_run_none(self):
        r = run({})
        assert r is None

    def test_bad_response(self):
        mock_response = Mock(status_code=404)
        mock_request = Mock(return_value=True,
                            **{"get.return_value": mock_response})
        with patch("attributes.attrib_github_date_last_committed.requests",
                   mock_request):
            r = run({"repo_url": "https://github.com/example"})
            assert r is None

    def test_good_response(self):
        timestamp = datetime.datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ')
        api_response = [
            {'commit': {'committer': {'date': timestamp}}}
        ]
        mock_response = Mock(status_code=200,
                             **{'json.return_value': api_response})
        mock_request = Mock(return_value=True,
                            **{"get.return_value": mock_response})
        with patch("attributes.attrib_github_date_last_committed.requests",
                   mock_request):
            r = run({"repo_url": "https://github.com/example"})
            assert r == {'name': ATTRIBUTE_SLUG, 'value': 0}


class TestAttribGitHubDateLastCommittedScore():
    def test_score_none(self):
        assert score({}) == []

    def test_score(self):
        project = [
            {'name': ATTRIBUTE_SLUG, 'value': 5,
             'project_score_attribute_id': 23}
        ]
        assert score(project) == [
            (ATTRIBUTE_SLUG, WEIGHT, 23, 5),
        ]
