from django.contrib import admin

from score.models import ProjectScore


class ProjectScoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProjectScore, ProjectScoreAdmin)
