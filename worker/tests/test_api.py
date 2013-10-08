from mock import Mock, patch
from api import get_score_attribute


class TestGetScoreAttribute():
    def test_no_slug(self):
        assert get_score_attribute("") is None

    def test_slug_valid(self):
        mock_response = Mock(status_code=200, **{'json.return_value': 'good'})
        mock_request = Mock(return_value=True,
                            **{"get.return_value": mock_response})
        with patch("api.requests", mock_request):
            r = get_score_attribute("good-slug")
            assert mock_request.get.call_count == 1
            assert mock_response.json.call_count == 1
            assert r == 'good'

    def test_slug_invalid(self):
        mock_response = Mock(status_code=404)
        mock_request = Mock(return_value=True,
                            **{"get.return_value": mock_response})
        with patch("api.requests", mock_request):
            r = get_score_attribute("good-slug")
            assert mock_request.get.call_count == 1
            assert mock_response.json.call_count == 0
            assert r is None
