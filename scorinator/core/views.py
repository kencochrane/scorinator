from django.views.generic import TemplateView
from score.models import ProjectScore
from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required
from project.models import Project


@login_required
@render_to('build_all.html')
def build_all(request):
    """
    This rebuilds all projects
    """
    projects = Project.objects.all()
    for project in projects:
        project.rebuild_score()
    return {}


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        top_scores = ProjectScore.objects.top(11)
        if top_scores:
            featured_project = list(top_scores).pop().project
        else:
            featured_project = {"name": "Unknown"}
        kwargs.update(featured_project=featured_project)
        kwargs.update(top_scores=top_scores)
        return super(HomeView, self).get_context_data(**kwargs)
