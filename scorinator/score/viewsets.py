from rest_framework import viewsets

from .models import ProjectScore, ScoreAttribute, ProjectScoreAttribute
from .serializers import (ScoreAttributeSerializer, ProjectScoreSerializer,
    ProjectScoreAttributeSerializer)


class ProjectScoreViewSet(viewsets.ModelViewSet):

    model = ProjectScore
    serializer_class = ProjectScoreSerializer


class ScoreAttributeViewSet(viewsets.ModelViewSet):

    model = ScoreAttribute
    serializer_class = ScoreAttributeSerializer


class ProjectScoreAttribute(viewsets.ModelViewSet):

    model = ProjectScoreAttribute
    serializer_class = ProjectScoreAttributeSerializer
