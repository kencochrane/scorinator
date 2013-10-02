import os
import sys

from django.conf import settings


def pytest_configure(config):
    here = os.path.join(os.path.dirname(__file__), "scorinator")
    sys.path.insert(0, here)
    here = os.path.join(os.path.dirname(__file__), "worker")
    sys.path.insert(0, here)

    if not settings.configured:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'scorinator.settings.test'
