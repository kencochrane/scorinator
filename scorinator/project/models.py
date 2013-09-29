from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from core.queue import enqueue_analytics, enqueue_score
import json

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

    def save(self, *args, **kwargs):
        """Need to set slug, if saving for first time"""
        if not self.pk:
            self.slug = set_slug(self.name)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project.detail", args=[self.slug])

    @property
    def score(self):
        from score.models import ProjectScore
        pscore = ProjectScore.objects.latest_for_project(self.pk)
        if pscore is not None:
            return pscore.total_score
        else:
            return pscore

    @property
    def dict_val(self):
        """ return object as a dict """
        data = {'name': self.name,
                'project_id': self.pk,
                'repo_url': self.repo_url,
                'slug': self.slug}
        from score.models import ProjectScore
        pscore = ProjectScore.objects.latest_for_project(self.pk)
        if pscore is not None:
            data['project_score_id'] = pscore.pk
        return data

    @property
    def json_val(self):
        """ Get the json version of this project """
        return json.dumps(self.dict_val)

    def create_new_project_score(self):
        from score.models import ProjectScore
        project_score = ProjectScore()
        project_score.project = self
        project_score.save()
        return project_score

    def rebuild_score(self):
        """ Queue up a build request for this project """
        proj_dict = self.dict_val
        # create new score object
        project_score = self.create_new_project_score()
        # overwrite original one since this is a new score
        proj_dict['project_score_id'] = project_score.pk
        json_out = json.dumps(proj_dict)
        return enqueue_analytics(json_out)

    def recalculate_score(self):
        """ Queue up a recalculate request for this project """
        from score.models import ProjectScoreAttribute
        results = [x.results for x in ProjectScoreAttribute.objects.filter(
            project_score__project__pk=self.pk)]
        data = {'project': self.dict_val, 'results': results}
        return enqueue_score(json.dumps(data))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name
