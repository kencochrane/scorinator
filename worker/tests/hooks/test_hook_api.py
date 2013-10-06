import json

from api import API_URL, AUTH
from mock import patch, Mock
from hooks.hook_api import send_score, run


class TestSendScore():
    def test_send(self):
        project_score_id = 2
        score_attribute_id = 3
        result = "4"
        payload = {
            "score_attribute": score_attribute_id,
            "project_score": project_score_id,
            "score_value": None,
            "result": json.dumps(result)
        }
        mock_requests = Mock()
        with patch("hooks.hook_api.requests", mock_requests):
            send_score(score_attribute_id, project_score_id, result)
            mock_requests.post.assert_called_with(
                "{0}project-score-attributes/".format(API_URL),
                data=payload,
                auth=AUTH
            )


class TestRun():
    def test_no_project_score_id(self):
        project = {}
        result = []
        assert run(project, result) is None

    def test_send_score_skipped(self):
        project_score_id = 1
        project = {"project_score_id": project_score_id}
        score_attrib_slug = "slug"
        value = None
        result = {"value": value, 'name': score_attrib_slug}
        score_attrib_id = 3
        mock_get_score_attribute = Mock(return_value={"id": score_attrib_id})
        mock_send_score = Mock()
        with patch("hooks.hook_api.get_score_attribute",
                   mock_get_score_attribute):
            with patch("hooks.hook_api.send_score", mock_send_score):
                assert run(project, result) == result
                mock_get_score_attribute.assert_called_with(score_attrib_slug)
                mock_send_score.call_count == 0

    def test_run(self):
        project_score_id = 1
        project = {"project_score_id": project_score_id}
        score_attrib_slug = "slug"
        value = True
        result = {"value": value, 'name': score_attrib_slug}
        score_attrib_id = 3
        mock_get_score_attribute = Mock(return_value={"id": score_attrib_id})
        mock_send_score = Mock()
        with patch("hooks.hook_api.get_score_attribute",
                   mock_get_score_attribute):
            with patch("hooks.hook_api.send_score", mock_send_score):
                r = run(project, result)
                result.update(project_score_attribute_id=score_attrib_id)
                assert r == result
                mock_get_score_attribute.assert_called_with(score_attrib_slug)
                mock_send_score.assert_called_with(score_attrib_id,
                                                   project_score_id, value)
