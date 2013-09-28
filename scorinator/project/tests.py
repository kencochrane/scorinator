from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django_dynamic_fixture import G

from project.models import Project, set_slug


class TestSetSlug(TestCase):
    def setUp(self):
        G(Project, name="test")

    def test_normal(self):
        assert "example" == set_slug("example")

    def test_first_dup(self):
        assert "test--1" == set_slug("test")

    def test_next_dup(self):
        G(Project, n=14, name="test2")
        assert Project.objects.filter(slug="test2--13").exists() is True


class TestProject(TestCase):
    def test_ordering(self):
        p = G(Project, name="AAAbc")
        G(Project, name="zxy")
        G(Project, name="mnc")

        assert Project.objects.all()[0] == p


class TestProjectListView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse("project.list"))
        assert response.status_code == 200

    def test_search(self):
        G(Project, name="Super Project")
        G(Project, name="Sucky Project")

        response = self.client.get(
            "{0}?name=super".format(reverse("project.list"))
        )
        assert "Super Project" in response.content
        assert "Sucky Project" not in response.content