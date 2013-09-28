import unittest

from django.core.urlresolvers import reverse
from django.test import RequestFactory
from django.test.client import Client
from django_dynamic_fixture import G

from project.models import Project
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

    def test_featured_project(self):
        p = G(Project, name="Super Project", slug="project")
        G(ProjectScore, project=p, total_score="55")

        response = self.client.get(reverse("home"))
        assert response.status_code == 200
        assert "Super Project" in response.content
