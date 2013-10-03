from attributes.attrib_github1 import (run, ATTRIBUTE_SLUG_REPO_FORKS,
                                       ATTRIBUTE_SLUG_REPO_WATCHERS,
                                       ATTRIBUTE_SLUG_REPO_OPEN_ISSUES)
from mock import Mock, patch


class TestAttribGitHub1Run():
    def test_run_none(self):
        r = run({})
        assert r is None

    def test_bad_response(self):
        mock_response = Mock(status_code=404)
        mock_request = Mock(return_value=True,
                            **{"get.return_value": mock_response})
        with patch("attributes.attrib_github1.requests", mock_request):
            r = run({"repo_url": "https://github.com/example"})
            assert r is None

    def test_good_response(self):
        response = {
            "watchers_count": 5,
            "open_issues_count": 20,
            "forks_count": 3
        }
        mock_response = Mock(status_code=200,
                             **{'json.return_value': response})
        mock_request = Mock(return_value=True,
                            **{"get.return_value": mock_response})
        with patch("attributes.attrib_github1.requests", mock_request):
            r = run({"repo_url": "https://github.com/example"})
            assert r == [
                {'name': ATTRIBUTE_SLUG_REPO_WATCHERS,
                 'value': 5},
                {'name': ATTRIBUTE_SLUG_REPO_FORKS,
                 'value': 3},
                {'name': ATTRIBUTE_SLUG_REPO_OPEN_ISSUES,
                 'value': 20},
            ]
