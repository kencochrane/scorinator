from django.conf.urls import patterns, include, url

from .views import github_hook


urlpatterns = patterns(
    '',
    url(r'^github/$', github_hook, name='github_hook'),
)
