from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from core.views import HomeView
from project.viewsets import ProjectViewSet
from score.viewsets import (
    ProjectScoreViewSet, ScoreAttributeViewSet, ProjectScoreAttribute)


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'project-scores', ProjectScoreViewSet)
router.register(r'score-attributes', ScoreAttributeViewSet)
router.register(r'project-score-attributes', ProjectScoreAttribute)

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^project/', include('project.urls')),

    # TODO we may want to disable this later post development.
    #  for now, it's useful to understand what is available
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^__admin__/', include(admin.site.urls)),
)
