#!/usr/bin/env python

import os
import sys
from traceback import format_exception
import time
import shutil
import logging
import json
import errno
from queue import queue_analytics_daemon
from git import clone_tmp

root_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(root_path, 'lib'))
logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger('worker')

# where we will clone repos under
REPO_DIR = "/tmp/repos"
# if we want to keep repos around after, useful for debugging.
CLEAN_UP = True


def mkdir_p(path):
    """ mkdir -p clone in python """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else:
            raise


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
    if not hasattr(mod, 'run'):
        logger.warning('{0} has no entry point.'.format(mod.__name__))
        return
    retry = 3
    result = None
    while retry > 0:
        try:
            mod.logger = logger
            result = mod.run(*args)
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
    result['timestamp'] = int(time.time())
    logger.info('{0}: finished'.format(mod.__name__))
    for hook in load_modules('hooks', 'hook'):
        run_module(hook, project, result.copy())


def run_analytics(project):
    full_results = []
    for mod in load_modules('attributes', 'attrib'):
        result = run_module(mod, project)
        if not result:
            logger.error('{0}: did not return any result'.format(mod.__name__))
            continue
        if isinstance(result, list):
            # if the module returned a list, process one at a time.
            for res in result:
                full_results.append(res)
                process_result(mod, project, res)
        else:
            # it was a dict result process like normal.
            full_results.append(result)
            process_result(mod, project, result)
    return full_results


def clean_repo_url(project):
    current_repo_url = project.get('repo_url', None)
    if current_repo_url and current_repo_url.startswith("https://github.com/"):
        if not current_repo_url.endswith(".git"):
            logger.info('adding .git to url {0}'.format(current_repo_url))
            repo_url = "{0}.git".format(current_repo_url)
        else:
            logger.info('Leaving gh url alone {0}'.format(current_repo_url))
            repo_url = current_repo_url
    else:
        logger.info('Leaving repo url alone {0}'.format(current_repo_url))
        repo_url = current_repo_url
    return repo_url


def clone_project(project):
    """ Clone the project locally """
    # todo actually do the clone
    repo_url = clean_repo_url(project)
    project_directory = clone_tmp(repo_url, base_dir=REPO_DIR)
    logging.info("Cloned repo dir = {0}".format(project_directory))
    return project_directory


def pre_job(project):
    """ run before it gets started. alter project input if needed"""
    project_directory = clone_project(project)
    project['project_directory'] = project_directory
    return project


def post_job(project, post_results):
    """ runs after the project is finished processing"""
    proj_dir = project.get('project_directory', None)
    if not proj_dir:
        return
    if os.path.isdir(proj_dir) and os.path.exists(proj_dir):
        logging.info("{0} exists".format(proj_dir))
        if CLEAN_UP:
            shutil.rmtree(proj_dir)
            logging.info("{0} removed".format(proj_dir))


def handle_job(project):
    logger.info('Starting... {0}'.format(project))
    project = json.loads(project)
    logger.debug("project json = {0}".format(project))
    project = pre_job(project)
    results = run_analytics(project)
    post_job(project, results)
    logger.info('Finsihed... {0}'.format(project))


def run():
    #TODO: add multi workers to speed things up.
    try:
        logger.info('make repo directory {0}'.format(REPO_DIR))
        mkdir_p(REPO_DIR)
        logger.info('start daemon')
        queue_analytics_daemon(handle_job)
    except Exception as e:
        (etype, value, tb) = sys.exc_info()
        print(etype)
        print(value)
        print(tb)
        trace_exception = ''.join(format_exception(etype, value, tb))
        print(trace_exception)
        logger.error('exception', "ERROR: {0}".format(trace_exception))
        logger.error(e)

if __name__ == '__main__':
    logger.info('Starting worker')
    run()
