from django.test import TestCase
from django_dynamic_fixture import G

from score.models import ProjectScore


class TestProjectScoreManager(TestCase):
    def setUp(self):
        self.p1 = G(ProjectScore, project_id=2, total_score=90)
        self.p2 = G(ProjectScore, project_id=1, total_score=100)
        self.p3 = G(ProjectScore, project_id=3, total_score=10)

    def test_top(self):
        assert list(ProjectScore.objects.top(1)) == [self.p2]

    def test_top_list(self):
        assert list(ProjectScore.objects.top(2)) == [self.p2, self.p1]

    # def test_top_list_extra(self):
    #     #test
    #     print(list(ProjectScore.objects.top(20)))
    #     assert list(ProjectScore.objects.top(20)) == [self.p2, self.p1, self.p3]