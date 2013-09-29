import os
import logging
from redis import Redis, StrictRedis


logger = logging.getLogger('worker')

def get_redis():
    if 'REDIS_HOST' in os.environ:
        logger.info("REDIS host = {0}".format(os.environ['REDIS_HOST']))
        redis = StrictRedis(host=os.environ['REDIS_HOST'],
                            port=int(os.environ['REDIS_PORT']),
                            db=0,
                            password=os.environ['REDIS_PASSWORD'])
    else:
        logger.info("REDIS host = localhost")
        redis = Redis()
    return redis

QUEUE_ANALYTICS_KEY = "scorinator_list"
QUEUE_SCORE_KEY = "scorinator_score"


def enqueue_analytics(value):
    return get_redis().rpush(QUEUE_ANALYTICS_KEY, value)


def enqueue_score(value):
    return get_redis().rpush(QUEUE_SCORE_KEY, value)


def queue_analytics_daemon(func):
    """ pass in the function that you want to process the
        result from the queue with."""
    logger.info("start queue_analytics_daemon")
    while 1:
        msg = get_redis().blpop(QUEUE_ANALYTICS_KEY)
        func(msg[1])


def queue_score_daemon(func):
    """ pass in the function that you want to process the
        result from the queue with."""
    while 1:
        msg = get_redis().blpop(QUEUE_SCORE_KEY)
        func(msg[1])


def print_worker(value):
    """ print value worker"""
    print(value)


def example():
    """ Example on how to process queue with a worker"""
    queue_analytics_daemon(print_worker)


# ## example script to kick off worker daemon
# #!/usr/bin/env python
# from common.queue import example
# example()
