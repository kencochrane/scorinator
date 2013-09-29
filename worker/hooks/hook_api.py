import os
import json
import requests
from requests.auth import HTTPBasicAuth


if 'API_URL' in os.environ:
    API_URL = os.environ['API_URL']
    API_USER = os.environ['API_USER']
    API_PASSWORD = os.environ['API_PASSWORD']
else:
    API_URL = "http://localhost:8000/api/v1/"
    API_USER = "ken"
    API_PASSWORD = "emily"

AUTH = HTTPBasicAuth(API_USER, API_PASSWORD)


def get_score_attribute(slug):
    """ query API to get the data we need """
    #TODO: Add some caching
    if not slug:
        return None
    r = requests.get("{0}score-attributes/has_readme/".format(API_URL), auth=AUTH)
    if r and r.status_code == 200:
        return r.json()
    else:
        return None


def send_score(score_attrib_id, project_score_id, value):
    """ Send the score to the API"""
    value = json.dumps(value)
    payload = {
        "score_attribute": score_attrib_id,
        "project_score": project_score_id,
        "score_value": None,
        "result": value,
    }
    r = requests.post("{0}project-score-attributes/".format(API_URL), data=payload, auth=AUTH)
    print(r.text)


def run(project, result):
    """ given a result, call the api with the results"""
    project_score_id = project.get('project_score_id', None)
    if not project_score_id:
        print("No project_score_id :(")
        return
    score_attrib_slug = result.get('name', None)
    score_attrib = get_score_attribute(score_attrib_slug)
    score_attrib_id = score_attrib.get('id', None)
    value = result.get('value', None)

    if score_attrib_id and project_score_id and value:
        send_score(score_attrib_id, project_score_id, value)
    else:
        print("Skip")
    print("Done")
    