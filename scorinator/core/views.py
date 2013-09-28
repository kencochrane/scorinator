from django.views.generic import TemplateView
from score.models import ProjectScore

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        top_scores = ProjectScore.objects.top(11)
        if top_scores:
            featured_project = top_scores.pop().project
        else:
            featured_project = {"name": "Unknown"}
        kwargs.update(featured_project=featured_project)
        kwargs.update(top_scores=top_scores)
        return super(HomeView, self).get_context_data(**kwargs)
