Worker
======

There are 2 workers (analytics, score). Theses workers listens to redis queues, and pull json objects off and processes them, sending the results back to the website via an API.

It gets the REDIS_HOST, REDIS_PORT, REDIS_PASSWORD via env variables that need to be set in order to run.


Get them working
----------------

$ python run.py
$ ptyhon calculator.py


Adding a new attribute to the worker
------------------------------------

In the worker/attributes directory add python file that looks like attrib_{*}.py and replace the {*} with the name of your test.

The python file needs to have a run function that takes a project object. It needs to return a dict of values, the key for the dict needs to return the following

   {
      'name': 'has_readme',   # the slug name for the scoreattribute in the database.
      'value': True           #
   }

When you put a new python attribute file, you will need to restart the workers and they will automatically pick them up and run them for the next run.
