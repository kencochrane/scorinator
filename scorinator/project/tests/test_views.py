import pytest

from django.core.urlresolvers import reverse
from django_dynamic_fixture import G
from django_webtest import WebTest
from project.models import Project
from score.models import ProjectScore


@pytest.mark.django_db
class TestProjectListView(WebTest):
    def test_get(self):
        response = self.app.get(reverse("project.list"))
        assert response.status_code == 200

    def test_search(self):
        G(Project, name="Super Project")
        G(Project, name="Sucky Project")

        response = self.app.get(
            "{0}?name=super".format(reverse("project.list"))
        )
        assert "Super Project" in response.content
        assert "Sucky Project" not in response.content


@pytest.mark.django_db
class TestProjectDetailView(WebTest):
    def test_no_score(self):
        p = G(Project, name="super project", slug="super")
        response = self.app.get(reverse("project.detail", args=[p.slug]))
        assert response.status_code == 200

    def test_with_score(self):
        p = G(Project, name="super project", slug="super")
        G(ProjectScore, project=p, total_score=65)
        response = self.app.get(reverse("project.detail", args=[p.slug]))
        assert response.status_code == 200
