import os
import requests

ATTRIBUTE_SLUG_REPO_WATCHERS = 'repo_watchers'
ATTRIBUTE_SLUG_REPO_FORKS = 'repo_forks'
ATTRIBUTE_SLUG_REPO_OPEN_ISSUES = 'open_issues_count'
WEIGHT = 10


def run(project):
    """ Look to see if a project has a readme file """
    repo_url = project.get('repo_url', None)
    if not repo_url:
        return None

    repo_url = repo_url.replace("github.com/", "api.github.com/repos/")

    r = requests.get(repo_url)
    if r and r.status_code == 200:
        data = r.json()
        watchers_count = data.get('watchers_count', None)
        open_issues_count = data.get('open_issues_count', None)
        repo_forks = data.get('forks_count', None)
    else:
        return None

    return [
                {'name': ATTRIBUTE_SLUG_REPO_WATCHERS, 'value': watchers_count},
                {'name': ATTRIBUTE_SLUG_REPO_FORKS, 'value': repo_forks},
                {'name': ATTRIBUTE_SLUG_REPO_OPEN_ISSUES, 'value': open_issues_count},
            ]

def score(project):
    return