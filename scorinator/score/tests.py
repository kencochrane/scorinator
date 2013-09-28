from django.test import TestCase

from score.templatetags.score_tags import display_score


class TestDisplayScore(TestCase):
    def test_danger(self):
        assert "danger" in display_score("30")

    def test_warning(self):
        assert "warning" in display_score("50")

    def test_primary(self):
        assert "primary" in display_score("65")

    def test_info(self):
        assert "info" in display_score("79")

    def test_success(self):
        assert "success" in display_score("81")
