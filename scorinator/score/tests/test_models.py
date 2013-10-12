import pytest

from django_dynamic_fixture import G
from score.models import ProjectScore, ScoreAttribute, ProjectScoreAttribute


@pytest.fixture
def projects():
    p1 = G(ProjectScore, project__id=2, total_score=90)
    p2 = G(ProjectScore, project__id=1, total_score=100)
    p3 = G(ProjectScore, project__id=3, total_score=10)
    return {'p1': p1, 'p2': p2, 'p3': p3}


@pytest.mark.django_db
class TestProjectScoreManager():
    def test_top(self, projects):
        assert list(ProjectScore.objects.top(1)) == [projects['p2']]

    def test_top_list(self, projects):
        assert list(ProjectScore.objects.top(2)) == [projects['p2'],
                                                     projects['p1']]

    def test_top_list_extra(self, projects):
        assert list(ProjectScore.objects.top(20)) == [
            projects['p2'], projects['p1'], projects['p3']]

    def test_recent(self, projects):
        assert list(ProjectScore.objects.recent()) == [
            projects['p3'], projects['p2'], projects['p1']]

    def test_recent_limit(self, projects):
        assert list(ProjectScore.objects.recent(1)) == [projects['p3']]

    def test_graded(self, projects):
        G(ProjectScore, project__id=2, total_score=100)
        assert ProjectScore.objects.graded() == 3

    def test_latest_for_project_first(self, projects):
        l = G(ProjectScore, project__id=2, total_score=100)
        assert list(ProjectScore.objects.latest_for_project(2, 1)) == [l]

    def test_latest_for_project(self, projects):
        l = G(ProjectScore, project__id=2, total_score=100)
        assert list(
            ProjectScore.objects.latest_for_project(2)) == [l, projects['p1']]

    def test_latest_for_project_none(self, projects):
        assert list(ProjectScore.objects.latest_for_project(99)) == []


@pytest.mark.django_db
class TestProjectScore():
    def test_str(self, projects):
        assert str(projects['p1']) == "{0} 90".format(
            projects['p1'].project.name)


@pytest.mark.django_db
class TestScoreAttribute():
    def test_str(self):
        s = G(ScoreAttribute, name="attrib", slug="s-attrib")
        assert str(s) == "s-attrib"


@pytest.mark.django_db
class TestProjectScoreAttributeManager():
    def test_for_score(self):
        p = G(ProjectScore)
        s = G(ProjectScoreAttribute, project_score=p, score_value=10)
        t = G(ProjectScoreAttribute, score_value=5)
        scores = ProjectScoreAttribute.objects.for_score(p.pk)
        assert s in scores
        assert t not in scores


@pytest.mark.django_db
class TestProjectScoreAttribute():
    def test_string(self):
        s = G(ProjectScoreAttribute, score_attribute__slug="slug",
              project_score__total_score=100, score_value=10)
        assert str(s) == "slug {0} 100 10".format(s.project_score.project)
