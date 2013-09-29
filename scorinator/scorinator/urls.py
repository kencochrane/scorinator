from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from core.views import HomeView, build_all
from project.viewsets import ProjectViewSet
from score.viewsets import (
    ProjectScoreViewSet, ScoreAttributeViewSet, ProjectScoreAttribute,
    ScoreAttributeDetail, ProjectScoreAttributeViewset)


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'project-scores', ProjectScoreViewSet)
router.register(r'score-attributes', ScoreAttributeViewSet)
router.register(r'project-score-attributes', ProjectScoreAttributeViewset)

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^hook/', include('hooks.urls')),
    url(r'^project/', include('project.urls')),

    #TODO: this is a little hack to get the query by slug,
    #      replace with better way later
    url(r'^api/v1/score-attributes/(?P<slug>[\w-]+)/$',
        ScoreAttributeDetail.as_view()),
    url(r'^api/v1/', include(router.urls)),
    url(r'^__admin__/', include(admin.site.urls)),
    url(r'^__buildall__/', build_all, name="build_all"),

)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^api-auth/', include('rest_framework.urls',
                                   namespace='rest_framework'))
    )
