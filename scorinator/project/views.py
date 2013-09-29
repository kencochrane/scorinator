from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from project.forms import ProjectForm
from project.models import Project


class ProjectListView(ListView):
    template_name = "project/project_list.html"
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        qs = super(ProjectListView, self).get_queryset()
        if "name" in self.request.GET:
            qs = qs.filter(name__icontains=self.request.GET.get("name"))
        return qs


class ProjectAddView(CreateView):
    template_name = "project/project_add.html"
    form_class = ProjectForm
    model = Project


class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = Project

    def get_context_data(self, **kwargs):
        from score.models import ProjectScoreAttribute
        if self.object.score:
            kwargs.update(
                score_breakdown=ProjectScoreAttribute.objects.for_score(
                    self.object.pk
                )
            )
        return super(ProjectDetailView, self).get_context_data(**kwargs)