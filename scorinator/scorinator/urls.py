from django.conf.urls import patterns, include, url

from core.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^project/', include('project.urls')),

    # TODO we may want to disable this later post development.
    #  for now, it's useful to understand what is available
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
)
