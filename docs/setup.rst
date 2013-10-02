=====
Setup
=====

Setting up a local development environment
------------------------------------------

1. Clone the repository

.. code-block:: bash

    $ git clone git@github.com:kencochrane/scorinator.git


2. Create the virtual environment

.. code-block:: bash

    $ mkvirtualenv scorinator


3. Install requirements

.. code-block:: bash

    $ pip install -r requirements/install.txt
    $ pip install -r requirements/testing.txt


4. Create the initial database structures with syncdb

.. code-block:: bash

    $ python scorinator/manage.py syncdb --settings=scorinator.settings.local


5. Create project related database structures and changes with migrate

.. code-block:: bash

    $ python scorinator/manage.py migrate --settings=scorinator.settings.local


6. Run the local server

.. code-block:: bash

    $ python scorinator/manage.py runserver --settings=scorinator.settings.local


7. Run tests

.. code-block:: bash

    $ py.test


Setting up a live environment
-----------------------------

TODO ansible, herku, digital ocean, etc...
