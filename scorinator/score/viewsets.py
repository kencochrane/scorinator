from django.http import Http404

from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProjectScore, ScoreAttribute, ProjectScoreAttribute
from .serializers import (
    ScoreAttributeSerializer, ProjectScoreSerializer,
    ProjectScoreAttributeSerializer)


class ProjectScoreViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    model = ProjectScore
    serializer_class = ProjectScoreSerializer


class ScoreAttributeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    model = ScoreAttribute
    serializer_class = ScoreAttributeSerializer


class ProjectScoreAttribute(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    model = ProjectScoreAttribute
    serializer_class = ProjectScoreAttributeSerializer

class ScoreAttributeDetail(APIView):
    """
    Retrieve, score attrribute instance.
    """
    def get_object(self, slug):
        try:
            return ScoreAttribute.objects.get(slug=slug)
        except ScoreAttribute.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        score = self.get_object(slug)
        serializer = ScoreAttributeSerializer(score)
        return Response(serializer.data)