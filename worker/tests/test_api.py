from api import get_score_attribute


class TestGetScoreAttribute():
    def test_no_slug(self):
        assert get_score_attribute("") == None
