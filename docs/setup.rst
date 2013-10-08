=====
Setup
=====

Setting up a local development environment
==========================================

Set up Environment
------------------

1. Clone the repository

.. code-block:: bash

    $ git clone git@github.com:kencochrane/scorinator.git


2. Create the virtual environment

.. code-block:: bash

    $ mkvirtualenv scorinator


Set up WebSite
--------------

1. Install requirements

.. code-block:: bash

    $ pip install -r requirements/install.txt
    $ pip install -r requirements/testing.txt


2. Create the initial database structures with syncdb

.. code-block:: bash

    $ python scorinator/manage.py syncdb --settings=scorinator.settings.local


3. Create project related database structures and changes with migrate

.. code-block:: bash

    $ python scorinator/manage.py migrate --settings=scorinator.settings.local


4. Run the local server

.. code-block:: bash

    $ python scorinator/manage.py runserver --settings=scorinator.settings.local


Set up Workers
--------------

1. Install requirements

.. code-block:: bash

    $ pip install -r worker/requirements.txt


2. Update api access params. Edit file ``worker/api.py`` and update the
variables to match the user setup in the database.

.. code-block:: python

    API_USER = "admin"
    API_PASSWORD = "secret"


3. Ensure REDIS is running locally


4. Run the workers

.. code-block:: bash

    $ python worker/run.py
    $ python worker/calcualtor.py


Running Tests
-------------

1. Run all tests

.. code-block:: bash

    $ py.test


Setting up a live environment
-----------------------------

TODO ansible, herku, digital ocean, etc...
