from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from project.forms import ProjectForm
from project.models import Project
from score.models import ProjectScore


class ProjectBuildView(DetailView):
    template_name = "project/project_build.html"
    model = Project

    def get_object(self):
        # Call the superclass
        the_object = super(ProjectBuildView, self).get_object()
        # Trigger the build
        the_object.rebuild_score()
        return the_object

    def get_context_data(self, **kwargs):
        from score.models import ProjectScoreAttribute
        if self.object.score:
            kwargs.update(
                score_breakdown=ProjectScoreAttribute.objects.for_score(
                    self.object.pk
                )
            )
        return super(ProjectBuildView, self).get_context_data(**kwargs)


class ProjectListView(ListView):
    template_name = "project/project_list.html"
    model = Project
    context_object_name = "projects"
    paginate_by = 10

    def get_queryset(self):
        qs = super(ProjectListView, self).get_queryset()
        if "name" in self.request.GET:
            qs = qs.filter(name__icontains=self.request.GET.get("name"))
        return qs


class ProjectAddView(CreateView):
    template_name = "project/project_add.html"
    form_class = ProjectForm
    model = Project

    # orginal way before build trigger keeping until we know both
    # work still
    #    def form_valid(self, form):
    #        form.instance.repo_url = form.cleaned_data['repo_url']
    #        return super(ProjectAddView, self).form_valid(form)

    def form_valid(self, form):
        """ save and then trigger score build """
        form.instance.repo_url = form.cleaned_data['repo_url']
        obj = form.save()
        obj.rebuild_score()
        url = reverse('project.detail', kwargs={'slug': obj.slug})
        return HttpResponseRedirect(url)


class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = Project

    def get_context_data(self, **kwargs):
        from score.models import ProjectScoreAttribute
        latest_scores = ProjectScore.objects.latest_for_project(
            self.object.pk, 10)
        if latest_scores:
            kwargs.update(
                score_breakdown=ProjectScoreAttribute.objects.for_score(
                    latest_scores[0].pk
                )
            )
        kwargs.update(latest_scores=[float(x.total_score)
                                     for x in latest_scores])
        return super(ProjectDetailView, self).get_context_data(**kwargs)
