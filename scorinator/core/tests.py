from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django_dynamic_fixture import G
from project.models import Project
from score.models import ProjectScore


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse("home"))
        assert response.status_code == 200

    def test_featured_project(self):
        p = G(Project, name="Awesome Project", slug="project")
        G(ProjectScore, project=p, total_score="55")

        response = self.client.get(reverse("home"))
        assert response.status_code == 200
        assert "Awesome Project" in response.content