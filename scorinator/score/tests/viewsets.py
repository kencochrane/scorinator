import unittest
from django.http import Http404

from django.test import RequestFactory
from score.viewsets import ScoreAttributeDetail


class ScoreAttributeDetailTest(unittest.TestCase):

    def setup_view(self, view, request, *args, **kwargs):
        """*args and **kwargs you could pass to ``reverse()``."""
        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view

    def setUp(self):
        self.view = self.setup_view(ScoreAttributeDetail(),
                                    RequestFactory().get('/'))

    def test_raise_404_on_missing_object(self):
        try:
            self.object = self.view.get_object("not-a-slug")
            self.fail("Expected an http404!")
        except Http404:
            pass