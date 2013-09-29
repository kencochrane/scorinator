from django.http import Http404

from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProjectScore, ScoreAttribute, ProjectScoreAttribute
from .serializers import (
    ScoreAttributeSerializer, ProjectScoreSerializer,
    ProjectScoreAttributeSerializer)


class ProjectScoreViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    model = ProjectScore
    serializer_class = ProjectScoreSerializer


class ScoreAttributeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    model = ScoreAttribute
    serializer_class = ScoreAttributeSerializer


class ProjectScoreAttribute(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    model = ProjectScoreAttribute
    serializer_class = ProjectScoreAttributeSerializer

    #def get_queryset(self):
    #    """
    #    score_attribute = models.ForeignKey(ScoreAttribute)
    #    project_score = models.ForeignKey(ProjectScore)
    #    """
    #    queryset = ProjectScoreAttribute.objects.all()
    #    score_attribute = self.request.QUERY_PARAMS.get('score_attribute', None)
    #    project_score = self.request.QUERY_PARAMS.get('project_score', None)
    #    if score_attribute is not None:
    #        queryset = queryset.filter(score_attribute__pk=score_attribute)
    #    if project_score is not None:
    #        queryset = queryset.filter(project_score__pk=project_score)
    #    return queryset


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
