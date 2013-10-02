import pytest

from django.test import TestCase
from django_dynamic_fixture import G
from project.models import Project, set_slug


@pytest.fixture
def project():
    return G(Project, name="test")

@pytest.mark.django_db
class TestSetSlug():
    def test_normal(self, project):
        assert "example" == set_slug("example")

    def test_first_dup(self, project):
        assert "test--1" == set_slug("test")

    def test_next_dup(self, project):
        G(Project, n=14, name="test2")
        assert Project.objects.filter(slug="test2--13").exists() is True


@pytest.mark.django_db
class TestProject(TestCase):
    def test_ordering(self):
        p = G(Project, name="AAAbc")
        G(Project, name="zxy")
        G(Project, name="mnc")

        assert Project.objects.all()[0] == p
