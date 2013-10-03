import datetime
import requests
import time

ATTRIBUTE_SLUG = 'repo_last_commit_days'
WEIGHT = 10


def run(project):
    """ Look to see if a project has a readme file """
    repo_url = project.get('repo_url', None)
    if not repo_url:
        return None

    repo_url = repo_url.replace("github.com/", "api.github.com/repos/")

    r = requests.get("{0}/commits".format(repo_url))
    if r and r.status_code == 200:
        try:
            last_commit = r.json()[-1]
            last_commit_string = last_commit['commit']['committer']['date']

            struct = time.strptime(last_commit_string, '%Y-%m-%dT%H:%M:%SZ')
            last_commit_date = datetime.datetime.fromtimestamp(
                time.mktime(struct)
            )

            today = datetime.datetime.utcnow()
            delta = today - last_commit_date
            days = delta.days
        except:
            # broad handling in case of trouble
            # TODO better testing yeilds narrower
            #  exception handling
            return None
    else:
        return None

    return {'name': ATTRIBUTE_SLUG, 'value': days}


def score(project):
    # day's might be -1 if there's a utc problem. We should treat this as 0

    # if commit in last day 10 points, last week 9 points last month 8 points
    # last 3 months 5 points, 6 months = 3, more then 6 , 0 points
    def determine_score(value):
        return WEIGHT

    results = []
    for attribute in project:
        svalue = 0
        rvalue = attribute['value']
        if attribute.get('name', False) == ATTRIBUTE_SLUG:
            svalue = determine_score(rvalue)
            results.append((ATTRIBUTE_SLUG,
                            svalue,
                            attribute.get('project_score_attribute_id'),
                            rvalue))
    return results
