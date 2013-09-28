import unittest
from django.core.urlresolvers import reverse

from django.test import RequestFactory
from django.test.client import Client
from django_dynamic_fixture import G

from project.models import Project, set_slug
from score.models import ProjectScore
from core.views import HomeView


class HomeTestCase(unittest.TestCase):
    """ Sample approach from: http://tech.novapost.fr/static/images/slides/
            djangocon-europe-2013-unit-test-class-based-views.html#slide13
    """
    def setup_view(self, view, request, *args, **kwargs):
        """*args and **kwargs you could pass to ``reverse()``."""
        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view

    def setUp(self):
        self.view = self.setup_view(HomeView(),
                                    RequestFactory().get('/'))
        self.template_names = self.view.get_template_names()
        self.context_data = self.view.get_context_data()
        self.client = Client()

    def test_get_template_names(self):
        self.assertEqual(self.template_names, ['index.html'])

    def test_context_data(self):
        self.assertIsNotNone(self.context_data['featured_project'])
        self.assertIsNotNone(self.context_data['top_scores'])


class TestHomeView(unittest.TestCase):
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


class TestSetSlug(unittest.TestCase):
    def setUp(self):
        G(Project, name="test")

    def test_normal(self):
        assert "example" == set_slug("example")

    def test_first_dup(self):
        assert "test--1" == set_slug("test")

    def test_next_dup(self):
        G(Project, n=14, name="test2")
        assert Project.objects.filter(slug="test2--13").exists() is True


class TestProject(unittest.TestCase):
    def test_ordering(self):
        p = G(Project, name="AAAbc")
        G(Project, name="zxy")
        G(Project, name="mnc")

        assert Project.objects.all()[0] == p


class TestProjectListView(unittest.TestCase):
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
