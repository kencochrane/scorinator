from django.db import models
from project.models import Project


class ProjectScoreManager(models.Manager):
    def top(self, limit=10):
        return self.get_query_set().filter(total_score__isnull=False)[0:limit]

    def latest_for_project(self, project_id):
        try:
            latest = self.get_query_set().filter(
                project__pk=project_id,
                total_score__isnull=False
            ).order_by("last_updated")[0]
        except IndexError:
            latest = None
        return latest


class ProjectScore(models.Model):
    project = models.ForeignKey(Project)
    total_score = models.DecimalField(max_digits=8, decimal_places=2,
                                      blank=True, null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = ProjectScoreManager()

    class Meta:
        ordering = ('total_score', )

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{0} {1}".format(self.project, self.total_score)


class ScoreAttribute(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.slug


class ProjectScoreAttributeManager(models.Manager):
    def for_score(self, project_score_id):
        return self.get_query_set().filter(project_score__pk=project_score_id)


class ProjectScoreAttribute(models.Model):
    score_attribute = models.ForeignKey(ScoreAttribute)
    project_score = models.ForeignKey(ProjectScore)
    score_value = models.DecimalField(max_digits=8, decimal_places=2,
                                      blank=True, null=True, default=None)
    result = models.TextField()

    objects = ProjectScoreAttributeManager()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{0} {1} {2}".format(self.score_attribute,
                                    self.project_score,
                                    self.score_value)
