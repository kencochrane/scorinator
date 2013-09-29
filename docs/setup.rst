=====
Setup
=====

Setting up a local development environment
------------------------------------------

1. Clone the repository

    $ git clone git@github.com:kencochrane/scorinator.git

2. Create the virtual environment

    $ mkvirtualenv scorinator

3. Install requirements

    $ pip install -r requirements.txt

4. Create the initial database structures with syncdb

    $ python scorinator/manage.py syncdb --settings=scorinator.settings.local

5. Create project related database structures and changes with migrate

    $ python scorinator/manage.py migrate --settings=scorinator.settings.local

6. Run the local server

    $ python scorinator/manage.py runserver --settings=scorinator.settings.local

