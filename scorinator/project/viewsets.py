from rest_framework import viewsets
from project.models import Project


class ProjectViewSet(viewsets.ModelViewSet):

    model = Project
