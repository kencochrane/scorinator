from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

DATABASES = {'default': dj_database_url.config()}

LOGGING['root'] = {
            'level': 'WARNING',
            'handlers': ['opbeat']}
LOGGING['loggers']['opbeat'] = {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False}
LOGGING['loggers']['opbeat.errors'] = {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False}

LOGGING['handlers']['log_file']['filename'] = '/var/log/scorinator.log'

ALLOWED_HOSTS=['localhost', 'scorinator.herokuapp.com']
