from rest_framework import viewsets, permissions

from .models import ProjectScore, ScoreAttribute, ProjectScoreAttribute
from .serializers import (
    ScoreAttributeSerializer, ProjectScoreSerializer,
    ProjectScoreAttributeSerializer)


class ProjectScoreViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    model = ProjectScore
    serializer_class = ProjectScoreAttributeSerializer


class ScoreAttributeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    model = ScoreAttribute
    serializer_class = ScoreAttributeSerializer


class ProjectScoreAttribute(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    model = ProjectScoreAttribute
    serializer_class = ProjectScoreSerializer
