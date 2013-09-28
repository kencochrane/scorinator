import random

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify


def set_slug(name):
    # make sure there are no duplicate slugs
    slug = slugify(unicode(name))
    if Project.objects.filter(slug=slug).exists():
        latest_slugs = Project.objects.values_list("slug", flat=True).filter(
            slug__startswith="{0}--".format(slug)
        )
        if latest_slugs:
            number = max(
                [int(j) for __, j in [x.rsplit("-", 1) for x in latest_slugs]]
            )
            number = int(number) + 1
        else:
            number = 1
        slug = "{slug}--{number}".format(slug=slug, number=number)
    return slug


class Project(models.Model):
    name = models.CharField(max_length=150)
    repo_url = models.URLField()
    description = models.TextField()
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Need to set slug, if saving for first time"""
        if not self.pk:
            self.slug = set_slug(self.name)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project.detail", args=[self.slug])

    def score(self):
        return random.randint(0, 100)

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return self.name