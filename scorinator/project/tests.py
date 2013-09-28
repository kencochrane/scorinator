from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django_dynamic_fixture import G

from project.models import Project


class TestProject(TestCase):
    def test_ordering(self):
        G(Project, name="abc")
        G(Project, name="zxy")
        G(Project, name="mnc")

        assert [p.name for p in Project.objects.all()] == ['abc', 'mnc', 'zxy']


class TestProjectListView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse("project.list"))
        assert response.status_code == 200
