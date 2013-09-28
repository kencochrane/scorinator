from django.conf.urls import patterns, url
from project.views import ProjectListView


urlpatterns = patterns('',
    url(r'^$', ProjectListView.as_view(), name="project.list"),
)
