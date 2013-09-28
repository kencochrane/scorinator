from django.core.urlresolvers import reverse
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=150)
    repo_url = models.URLField()
    description = models.TextField()
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )

    def get_absolute_url(self):
        return reverse("project.detail", args=[self.slug])