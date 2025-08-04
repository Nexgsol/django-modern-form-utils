#!/usr/bin/env python

import os
import sys
import django
from django.conf import settings


def configure_settings():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    settings.configure(
        DEBUG=True,
        SECRET_KEY='test-secret-key',
        BASE_DIR=BASE_DIR,
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'modern_form_utils',
            'tests',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
            }
        },
        MEDIA_ROOT=os.path.join(BASE_DIR, 'media'),
        MEDIA_URL='/media/',
        STATIC_URL='/static/',
        DEFAULT_AUTO_FIELD='django.db.models.AutoField',
        MIDDLEWARE=[],
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {},
        }],
    )


def runtests(*test_args):
    if not settings.configured:
        configure_settings()

    django.setup()

    if not test_args:
        test_args = ['tests']

    from django.test.runner import DiscoverRunner
    failures = DiscoverRunner(
        verbosity=1,
        interactive=True,
        failfast=False
    ).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
