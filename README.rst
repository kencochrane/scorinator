DjangoDash2013
==============

Authors
-------
- Ken Cochrane
- John Costa
- Greg Reinbach

Setup
-----

1. Create VE

.. code-block: bash

    $ mkvirtualenv scorinator

2. Install requirements

.. code-block: bash

    $ pip install -r requirements.txt

3. SyncDB

.. code-block: bash

    $ python manage.py syncdb --settings=scorinator.settings.local

4. migrate

.. code-block: bash

    $ python manage.py migrate --settings=scorinator.settings.local

5. run server

.. code-block: bash

    $ python manage.py runserver --settings=scorinator.settings.local
