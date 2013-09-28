from django.views.generic import ListView
from project.models import Project


class ProjectListView(ListView):
    template_name = "project/project_list.html"
    model = Project
    context_object_name = "projects"
