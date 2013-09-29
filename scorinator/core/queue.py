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
