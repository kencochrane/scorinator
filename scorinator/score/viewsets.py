from rest_framework import viewsets

from score.models import ProjectScore, ScoreAttribute, ProjectScoreAttribute


class ProjectScoreViewSet(viewsets.ModelViewSet):

    model = ProjectScore


class ScoreAttributeViewSet(viewsets.ModelViewSet):

    model = ScoreAttribute


class ProjectScoreAttribute(viewsets.ModelViewSet):

    model = ProjectScoreAttribute
