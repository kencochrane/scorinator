import logging
import simplejson as json

logger = logging.getLogger('worker')


def run(project, result):
    logger.info('HOOK PRINT: {0}:{1}'.format(
        project, json.dumps(result, indent=4)))
