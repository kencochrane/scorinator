import pytest

from django.core.urlresolvers import reverse
from django_webtest import WebTest


@pytest.mark.django_db
class TestScoreAttributeDetail(WebTest):
    def test_raise_404_on_missing_object(self):
        response = self.app.get(reverse("score.attributes",
                                        args=['not-a-slug']),
                                status=404)
        assert response.status_code == 404
