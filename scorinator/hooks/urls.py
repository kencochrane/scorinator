from django.conf.urls import patterns, url

from .views import github_hook


urlpatterns = patterns(
    '',
    url(r'^github/$', github_hook, name='github_hook'),
)
