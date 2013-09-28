import unittest

from django.test import RequestFactory

from..views import HomeView


class HomeTestCase(unittest.TestCase):

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

    def test_get_template_names(self):
        self.assertEqual(self.template_names, ['index.html'])

    def test_context_data(self):
        self.assertIsNotNone(self.context_data['featured_project'])
        self.assertIsNotNone(self.context_data['top_scores'])
