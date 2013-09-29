DjangoDash2013 - Scorinator
===========================

.. image:: https://travis-ci.org/kencochrane/scorinator.png?branch=master
  :target: https://travis-ci.org/kencochrane/scorinator

.. image:: https://coveralls.io/repos/kencochrane/scorinator/badge.png?branch=master
  :target: https://coveralls.io/r/kencochrane/scorinator?branch=master

Open source project scoring.

About
-----
The idea for this project was originally inspired by Daniel Greenfeld and Audrey Roy talk at DjangoCon 2011 called "Django Package Thunderdome: Is Your Package Worthy?" (http://lanyrd.com/2011/djangocon-us/shbqh/#link-fgxz). They did a lot of their analysis by hand, we hope to automate their process, and expand it to include more topics.

The goal of this project is to look at an open source project and give it a score using a rating system that we develop based on what we think makes a project good. We then take those attributes and create a score, and we use those scores to analyze other open source projects to see how well they rate, and what they need to do to improve their project.

Due to the lack of time in the djangoDash we couldn't add all the features that we wanted, and there is still a lot to improve on. We hope to add these features over time to improve the service. Our goal for DjangoDash was to put the foundation in place so that it is easy to work on it in the future.

Helping out
-----------
If you are interested in helping out, or you think this is a good idea, please let us know, or even better fork the project and start helping out.


website
-------
https://scorinator.herokuapp.com

Authors
-------
- Ken Cochrane
- John Costa
- Greg Reinbach

Requirements
------------

  * Python 2.7+ (Not tested with prior versions of python)
  * Django 1.5+ (Not tested with prior versions of django)


Documentation
-------------

You can build the documentation locally with the following:

::

    pip install sphinx
    cd docs
    make html

`Online documentation` is graciously provided by `ReadTheDocs`_.


Project Setup
-------------

The instructions for setting up a `local development project`_.


.. _Online documentation: http://scorinator.readthedocs.org/en/latest/
.. _ReadTheDocs: https://readthedocs.org/
.. _local development project: http://scorinator.readthedocs.org/en/latest/setup.html#setting-up-a-local-development-environment
