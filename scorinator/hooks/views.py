import json
import logging

from django.views.decorators.csrf import csrf_view_exempt
from django.http import (HttpResponse)

from project.models import Project

log = logging.getLogger(__name__)


@csrf_view_exempt
def github_hook(request):
    """
    github hook, when we get a request it will check to see if we have
    project already,
    if not, it will add it and trigger build. If we have it, it just
    triggers build.
    """
    log.debug("Github Hook")
    if request.method == 'POST':
        log.debug("Github Hook is POST")
        try:
            try:
                data = json.loads(request.POST['payload'])
            except Exception as exc:
                log.debug("(Github) parse request error = {0}".format(exc))
                return HttpResponse('Invalid payload')
            log.debug("-----")
            log.debug(data)
            log.debug("-----")
            repo = data.get('repository', {})
            name = repo.get('name', None)
            url = repo.get('url', "")
            url = url.replace('http://', 'https://')
            branch = data.get('ref', "").replace('refs/heads/', '')
            log.info("(Github Build) %s:%s" % (url, branch))

            try:
                project = Project.objects.get(repo_url=url)
                log.info("We have the project already {0}".format(project))
            except Project.DoesNotExist:
                log.info("New Project")
                project = Project()
                project.repo_url = url
                project.name = name
                project.save()
            log.info("Trigger build")
            project.rebuild_score()
        except Exception as exc:
            log.error("(Github) {0}".format(exc))
    else:
        log.debug("Github Hook was GET")
    log.info("Done webhook")
    return HttpResponse('Build Started')
