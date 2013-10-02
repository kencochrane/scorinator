from .base import *  # NOQA

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

EMAIL_SUBJECT_PREFIX = '[TEST] '
LOGGING['handlers']['log_file']['filename'] = '/tmp/scorinator-unittest.log'
