import requests
import logging

from api import AUTH, API_URL, get_score_attribute

logger = logging.getLogger('worker')


def send_score(project_score_attribute_id, score_attribute_id,
               project_score_id, value, result):
    """ Send the score to the API"""
    payload = {
        "project_score_attribute": project_score_attribute_id,
        "project_score": project_score_id,
        "score_attribute": score_attribute_id,
        "score_value": value,
        "result": result
    }
    r = requests.put("{0}project-score-attributes/{1}/".format(
        API_URL,
        project_score_attribute_id
    ), data=payload, auth=AUTH)
    logging.debug(r.text)


def score(project, result):
    """ given a result, call the api with the results"""
    project_score_id = project.get('project', {}).get('project_score_id', None)
    if not project_score_id:
        logging.info("No project_score_id :(")
    project_score_attribute_id = result[2]
    if not project_score_attribute_id:
        logging.info("No project_score_attribute_id :(")
        return
    score_attrib_slug = result[0]
    score_attrib = get_score_attribute(score_attrib_slug)
    score_attrib_id = score_attrib.get('id', None)
    value = result[1]

    if value:
        send_score(project_score_attribute_id, score_attrib_id,
                   project_score_id, value, result[3])
    else:
        logging.debug("Skip")
    logging.debug("Done")
