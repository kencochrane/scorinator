from rest_framework import viewsets

from score.models import ProjectScore, ScoreAttribute


class ProjectScoreViewSet(viewsets.ModelViewSet):

    model = ProjectScore


class ScoreAttributeViewSet(viewsets.ModelViewSet):

    model = ScoreAttribute
