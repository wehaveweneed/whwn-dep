from settings.common import *
import sys

TEST = 'test' in sys.argv or 'jenkins' in sys.argv

DEBUG = TEMPLATE_DEBUG = REQUIRE_DEBUG = True

POSTMARK_TEST_MODE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'whwn',
        'USER': 'whwn',
        'PASSWORD': 'whwn',
    },
}

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    }
}

PIPELINE_JS_COMPRESSOR = False
PIPELINE_CSS_COMPRESSOR = False
PIPELINE_COMPASS_BINARY = '/usr/bin/env compass'

# Celery Message Broker Options
BROKER_URL = "redis://localhost:6379/0"
BROKER_BACKEND = 'redis'
BROKER_VHOST = '1'
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://localhost:9200/',
        'INDEX_NAME': 'test' if TEST else 'haystack'
    },
}

# All testing and jenkins CI options
if TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

    SOUTH_TESTS_MIGRATE = False

    # Debug messages clutter up test report output
    import logging
    logging.disable(logging.INFO)

JENKINS_TASKS = (
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.dir_tests',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
)

# List of apps for jenkins to test
PROJECT_APPS = ['whwn']

# Absolute path to the directory media files should go to.
MEDIA_ROOT = project('media/')

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = "/tmp/whwn/static" 

# This secret key is only used for development
SECRET_KEY = "H6ikIpTviA5YMz+V2ZzB6XUOLvl370vFEw34ob2+"
