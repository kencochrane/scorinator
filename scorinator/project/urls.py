from django.conf.urls import patterns, url
from project.views import (ProjectListView, ProjectAddView, ProjectDetailView,
    ProjectBuildView)


urlpatterns = patterns(
    '',
    url(r'^$', ProjectListView.as_view(), name="project.list"),
    url(r'^add/$', ProjectAddView.as_view(), name="project.add"),
    url(r'^(?P<slug>[\w-]+)/$', ProjectDetailView.as_view(),
        name="project.detail"),
    url(r'^(?P<slug>[\w-]+)/build$', ProjectBuildView.as_view(),
        name="project.build"),
)
