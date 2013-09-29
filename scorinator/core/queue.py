import os
from redis import Redis, StrictRedis

if 'REDIS_HOST' in os.environ:
    redis = StrictRedis(host=os.environ['REDIS_HOST'],
                        port=int(os.environ['REDIS_PORT']),
                        db=0,
                        password=os.environ['REDIS_PASSWORD'])
else:
    redis = Redis()

QUEUE_ANALYTICS_KEY = "scorinator_list"
QUEUE_SCORE_KEY = "scorinator_score"


def enqueue_analytics(value):
    return redis.rpush(QUEUE_ANALYTICS_KEY, value)


def enqueue_score(value):
    return redis.rpush(QUEUE_SCORE_KEY, value)
