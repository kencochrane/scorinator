from django.conf.urls import patterns, url
from project.views import ProjectListView, ProjectAddView


urlpatterns = patterns(
    '',
    url(r'^$', ProjectListView.as_view(), name="project.list"),
    url(r'^add/$', ProjectAddView.as_view(), name="project.add"),
)
