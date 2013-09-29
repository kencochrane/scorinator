DjangoDash2013
==============

.. image:: https://travis-ci.org/kencochrane/scorinator.png?branch=master
  :target: https://travis-ci.org/kencochrane/scorinator

.. image:: https://coveralls.io/repos/kencochrane/scorinator/badge.png?branch=master
  :target: https://coveralls.io/r/kencochrane/scorinator?branch=master


Authors
-------
- Ken Cochrane
- John Costa
- Greg Reinbach

Setup
-----

1. Create VE

    $ mkvirtualenv scorinator

2. Install requirements

    $ pip install -r requirements.txt

3. SyncDB

    $ python manage.py syncdb --settings=scorinator.settings.local

4. migrate

    $ python manage.py migrate --settings=scorinator.settings.local

5. run server

    $ python manage.py runserver --settings=scorinator.settings.local

Docs
----

http://scorinator.readthedocs.org/en/latest/
