from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=150)
    repo_url = models.URLField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
