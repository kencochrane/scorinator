from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}

COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'runners$', 'manage$'
]
COVERAGE_MODULE_EXCLUDES += PREREQ_APPS
TEST_RUNNER = 'test.runners.OurCoverageRunner'
COVERAGE_REPORT_HTML_OUTPUT_DIR = 'reports'

EMAIL_SUBJECT_PREFIX = '[TEST] '
LOGGING['handlers']['log_file']['filename'] = '/tmp/scorinator-unittest.log'
