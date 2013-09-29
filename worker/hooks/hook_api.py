import json
import requests

from ..auth import AUTH, API_URL, get_score_attribute


def send_score(score_attrib_id, project_score_id, value):
    """ Send the score to the API"""
    value = json.dumps(value)
    payload = {
        "score_attribute": score_attrib_id,
        "project_score": project_score_id,
        "score_value": None,
        "result": value,
    }
    r = requests.post("{0}project-score-attributes/".format(API_URL),
                      data=payload, auth=AUTH)
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
