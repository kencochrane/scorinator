from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from project.forms import ProjectForm
from project.models import Project


class ProjectListView(ListView):
    template_name = "project/project_list.html"
    model = Project
    context_object_name = "projects"


class ProjectAddView(CreateView):
    template_name = "project/project_add.html"
    form_class = ProjectForm
    model = Project


class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = Project
