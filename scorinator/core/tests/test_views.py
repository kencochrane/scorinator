import pytest

from django.core.urlresolvers import reverse
from django_dynamic_fixture import G
from django_webtest import WebTest

from project.models import Project
from score.models import ProjectScore


@pytest.mark.django_db
class TestHomeView(WebTest):
    def test_get(self):
        response = self.app.get(reverse("home"))
        assert response.status_code == 200
        self.assertTemplateUsed('index.html')

    def test_featured_project(self):
        p = G(Project, name="Awesome Project", slug="project")
        G(ProjectScore, project=p, total_score="55")

        response = self.app.get(reverse("home"))
        assert response.status_code == 200
        assert "Awesome Project" in response.content
