import pytest

from django_dynamic_fixture import G
from score.models import ProjectScore
from score.templatetags.score_tags import (display_score,
                                           display_project_score,
                                           display_attribute_score,
                                           projects_scored)


@pytest.mark.django_db
class TestProjectsScored():
    def test_score(self):
        G(ProjectScore, n=4, total_score=10)
        G(ProjectScore, n=3, total_score=None)
        assert projects_scored() == 4


class TestDisplayScore():
    def test_string(self):
        value = "10"
        tag = "default"
        title = "title"
        r = display_score(value, tag, title)
        assert value in r
        assert tag in r
        assert title.capitalize() in r


class TestDisplayProjectScore():
    def test_string(self):
        assert "?" in display_project_score("")

    def test_none(self):
        assert "?" in display_project_score(None)

    def test_danger(self):
        assert "danger" in display_project_score("30")

    def test_warning(self):
        assert "warning" in display_project_score("50")

    def test_primary(self):
        assert "primary" in display_project_score("65")

    def test_info(self):
        assert "info" in display_project_score("79")

    def test_success(self):
        assert "success" in display_project_score("81")


class TestDisplayAttributeScore():
    def test_string(self):
        value = "10"
        assert value in display_attribute_score(value)
