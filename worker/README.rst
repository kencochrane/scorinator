Worker
======

The worker listens to a redis queue, and pulls json objects off and processes them and sends the results back to the website via an API.

It gets the REDIS_HOST, REDIS_PORT, REDIS_PASSWORD via env variables that need to be set in order to run.

Get it working
--------------

$ python run.py

