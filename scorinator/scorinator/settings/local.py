from .base import *  # NOQA

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# send emails to command line instead of via SMTP for all local emails.
# this is to make sure we don't accidently send emails out to people
# who shouldn't be getting them when doing local testing.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'scorinator.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '', }
}

INSTALLED_APPS += ('django_extensions',)
