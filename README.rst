DjangoDash2013
==============

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