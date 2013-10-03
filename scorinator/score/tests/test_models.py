import pytest

from django_dynamic_fixture import G
from score.models import ProjectScore


@pytest.fixture
def projects():
    p1 = G(ProjectScore, project_id=2, total_score=90)
    p2 = G(ProjectScore, project_id=1, total_score=100)
    p3 = G(ProjectScore, project_id=3, total_score=10)
    return {'p1': p1, 'p2': p2, 'p3': p3}


@pytest.mark.django_db
class TestProjectScoreManager():
    def test_top(self, projects):
        assert list(ProjectScore.objects.top(1)) == [projects['p2']]

    def test_top_list(self, projects):
        assert list(ProjectScore.objects.top(2)) == [projects['p2'],
                                                     projects['p1']]

    # def test_top_list_extra(self):
    #     #test
    #     print(list(ProjectScore.objects.top(20)))
    #     assert list(ProjectScore.objects.top(20)) == [self.p2,
    #    self.p1, self.p3]
