from api import API_URL, AUTH
from mock import patch, Mock
from score_hooks.hook_api import send_score, score


class TestSendScore():
    def test_send(self):
        project_score_attribute_id = 1
        project_score_id = 2
        score_attribute_id = 3
        value = True
        result = "4"
        payload = {
            "project_score_attribute": project_score_attribute_id,
            "project_score": project_score_id,
            "score_attribute": score_attribute_id,
            "score_value": value,
            "result": result
        }
        mock_requests = Mock()
        with patch("score_hooks.hook_api.requests", mock_requests):
            send_score(project_score_attribute_id, score_attribute_id,
                       project_score_id, value, result)
            mock_requests.put.assert_called_with(
                "{0}project-score-attributes/{1}/".format(
                    API_URL, project_score_attribute_id),
                data=payload,
                auth=AUTH)


class TestScore():
    def test_no_project_score_id(self):
        project = {}
        result = [None, None, None]
        assert score(project, result) is None

    def test_score_skipped(self):
        project_score_id = 1
        project = {"project": {"project_score_id": project_score_id}}
        value = None
        project_score_attribute_id = 2
        score_attrib_slug = "slug"
        final_result = 3
        result = [score_attrib_slug, value, project_score_attribute_id,
                  final_result]
        score_attrib_id = 3
        mock_get_score_attribute = Mock(return_value={"id": score_attrib_id})
        mock_send_score = Mock()
        with patch("score_hooks.hook_api.get_score_attribute",
                   mock_get_score_attribute):
            with patch("score_hooks.hook_api.send_score", mock_send_score):
                score(project, result)
                mock_get_score_attribute.assert_called_with(score_attrib_slug)
                mock_send_score.call_count == 0

    def test_score(self):
        project_score_id = 1
        project = {"project": {"project_score_id": project_score_id}}
        value = 1
        project_score_attribute_id = 2
        score_attrib_slug = "slug"
        final_result = 3
        result = [score_attrib_slug, value, project_score_attribute_id,
                  final_result]
        score_attrib_id = 3
        mock_get_score_attribute = Mock(return_value={"id": score_attrib_id})
        mock_send_score = Mock()
        with patch("score_hooks.hook_api.get_score_attribute",
                   mock_get_score_attribute):
            with patch("score_hooks.hook_api.send_score", mock_send_score):
                score(project, result)
                mock_get_score_attribute.assert_called_with(score_attrib_slug)
                mock_send_score.assert_called_with(
                    project_score_attribute_id,
                    score_attrib_id,
                    project_score_id,
                    value,
                    final_result
                )