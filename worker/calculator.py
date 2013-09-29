#!/usr/bin/env python

import os
import sys
import time
import logging
import json
import requests

from api import AUTH, API_URL
from queue import queue_score_daemon


root_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(root_path, 'lib'))
logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger('calculator')


def load_modules(path, prefix):
    for fname in os.listdir(os.path.join(root_path, path)):
        if not fname.startswith(prefix) or not fname.endswith('.py'):
            continue
        name = fname[:-3]
        try:
            mod = __import__(
                '{0}.{1}'.format(path, name), globals(), locals(), [name], -1)
            yield mod
        except Exception as e:
            logger.warning('Ignoring "{0}": {1}'.format(name, e))


def run_module(mod, *args):
    logger.info('{0}: started'.format(mod.__name__))
    if not hasattr(mod, 'score'):
        logger.warning('{0} has no entry point.'.format(mod.__name__))
        return
    retry = 3
    result = None
    while retry > 0:
        try:
            mod.logger = logger
            result = mod.score(*args)
            break
        except Exception:
            logger.exception(
                '{0}: returned an error.'
                ' Retrying in 1 second...'.format(mod.__name__))
            retry -= 1
            time.sleep(1)
            continue
    return result


def process_result(mod, project, result):
    """ given a result dictionary process it """
    logger.info('{0}: finished'.format(mod.__name__))
    for hook in load_modules('score_hooks', 'hook'):
        run_module(hook, project, result)


def run_scorer(project):
    full_results = []
    for mod in load_modules('attributes', 'attrib'):
        result = run_module(mod, project.get('results', []))
        if not result:
            logger.error('{0}: did not return any result'.format(mod.__name__))
            continue
        full_results.append(result)
        process_result(mod, project, result)
    return full_results


def post_job(project, post_results):
    """Total the score and send result to api"""
    total = 0
    for attribute, score in post_results:
        total += score
    logger.info('total score: {0}'.format(total))
    project_id = project.get('project', {}).get('project_id', None)
    if not project_id:
        logger.info("No project_id :(")
        return
    payload = {
        "project": project_id,
        "total_score": total,
    }
    r = requests.post("{0}project-scores/".format(API_URL),
                      data=payload, auth=AUTH)
    logger.debug(r.text)


def handle_job(project):
    logger.info('Starting... {0}'.format(project))
    project = json.loads(project)
    logger.debug("project json = {0}".format(project))
    results = run_scorer(project)
    post_job(project, results)
    logger.info('Finished... {0}'.format(results))


def run():
    #TODO: add multi workers to speed things up.
    try:
        queue_score_daemon(handle_job)
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    logger.info('Starting calculator')
    run()
