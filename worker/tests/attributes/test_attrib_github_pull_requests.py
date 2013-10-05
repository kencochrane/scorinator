from attributes.attrib_github_pull_requests import (run, score, WEIGHT,
                                                    ATTRIBUTE_SLUG)
from mock import Mock, patch


class TestAttribGitHubPullRequestsRun(object):
    def test_run_none(self):
        r = run({})
        assert r is None

    def test_bad_response(self):
        mock_response = Mock(status_code=404)
        mock_request = Mock(return_value=True,
                            **{"get.return_value": mock_response})
        with patch("attributes.attrib_github_pull_requests.requests",
                   mock_request):
            r = run({"repo_url": "https://github.com/example"})
            assert r is None

    def test_good_response(self):
        api_response = [1, 2, 3, 4]
        mock_response = Mock(status_code=200,
                             **{'json.return_value': api_response})
        mock_request = Mock(return_value=True,
                            **{"get.return_value": mock_response})
        with patch("attributes.attrib_github_pull_requests.requests",
                   mock_request):
            r = run({"repo_url": "https://github.com/example"})
            assert r == {'name': ATTRIBUTE_SLUG, 'value': 4}


class TestAttribGitHubPullRequestsScore():
    def test_score_none(self):
        assert score({}) == []

    def test_score_false(self):
        project = [{'name': ATTRIBUTE_SLUG, 'value': 0,
                   'project_score_attribute_id': 23}]
        assert score(project) == [(ATTRIBUTE_SLUG, 0, 23, 0)]

    def test_score(self):
        project = [
            {'name': ATTRIBUTE_SLUG, 'value': 5,
             'project_score_attribute_id': 23}
        ]
        assert score(project) == [
            (ATTRIBUTE_SLUG, WEIGHT, 23, 5),
        ]
