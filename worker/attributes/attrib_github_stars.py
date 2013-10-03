import requests

ATTRIBUTE_SLUG = 'repo_stars'
WEIGHT = 10


def run(project):
    """ Look to see if a project has a readme file """
    repo_url = project.get('repo_url', None)
    if not repo_url:
        return None

    repo_url = repo_url.replace("github.com/", "api.github.com/repos/")

    r = requests.get("{0}/stargazers".format(repo_url))
    if r and r.status_code == 200:
        repo_stars = len(r.json())
    else:
        return None

    return {'name': ATTRIBUTE_SLUG, 'value': repo_stars}


def score(project):
    results = []
    for attribute in project:
        svalue = 0
        rvalue = attribute['value']
        if attribute.get('name', False) == ATTRIBUTE_SLUG:
            if bool(rvalue):
                svalue = WEIGHT
            results.append((ATTRIBUTE_SLUG,
                            svalue,
                            attribute.get('project_score_attribute_id'),
                            rvalue))
    return results
