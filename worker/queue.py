import os
from redis import Redis, StrictRedis

if 'REDIS_HOST' in os.environ:
    redis = StrictRedis(host=os.environ['REDIS_HOST'],
                        port=int(os.environ['REDIS_PORT']),
                        db=0,
                        password=os.environ['REDIS_PASSWORD'])
else:
    redis = Redis()

QUEUE_KEY = "scorinator_list"


def enqueue(value):
    return redis.rpush(QUEUE_KEY, value)


def queue_daemon(func):
    """ pass in the function that you want to process the
        result from the queue with."""
    while 1:
        msg = redis.blpop(QUEUE_KEY)
        func(msg[1])


def print_worker(value):
    """ print value worker"""
    print(value)


def example():
    """ Example on how to process queue with a worker"""
    queue_daemon(print_worker)


# ## example script to kick off worker daemon
# #!/usr/bin/env python
# from common.queue import example
# example()
