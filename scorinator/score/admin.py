from django.contrib import admin

from score.models import ProjectScore, ScoreAttribute, ProjectScoreAttribute


class ProjectScoreAdmin(admin.ModelAdmin):
    pass


class ScoreAttributeAdmin(admin.ModelAdmin):
    pass

class ProjectScoreAttributeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectScore, ProjectScoreAdmin)
admin.site.register(ScoreAttribute, ScoreAttributeAdmin)
admin.site.register(ProjectScoreAttribute, ProjectScoreAttributeAdmin)
