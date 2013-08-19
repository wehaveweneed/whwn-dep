from settings.common import *

PIPELINE_COFFEE_SCRIPT_BINARY = '/app/node_modules/.bin/coffee'

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    "default": dj_database_url.config()
}

# Twilio options
TWILIO_SID    = os.getenv('WHWN_TWILIO_SID')
TWILIO_TOKEN  = os.getenv('WHWN_TWILIO_TOKEN')
TWILIO_NUMBER = os.getenv('WHWN_TWILIO_NUMBER')

# Postmark options
EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
POSTMARK_API_KEY = os.getenv('WHWN_POSTMARK_API_KEY')
DEFAULT_FROM_EMAIL = os.getenv('WHWN_DEFAULT_FROM_EMAIL')

AWS_ACCESS_KEY_ID = os.getenv('WHWN_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('WHWN_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('WHWN_BOTO_S3_BUCKET')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')

DEBUG = TEMPLATE_DEBUG = REQUIRE_DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))
PIPELINE = True
PIPELINE_CSS_COMPRESSOR = None
PIPELINE_COMPASS_BINARY = '/app/.heroku/ruby/bin/compass'
PIPELINE_DISABLE_WRAPPER = True
PIPELINE_TEMPLATE_FUNC = "_.template"
PIPELINE_JS_COMPRESSOR = None
PIPELINE_JS = {
    'app': {
        'source_filenames': (
            'vendor/js/jquery-1.8.2.js',
            'vendor/jqueryUI/js/jquery-ui-1.10.0.custom.js',
            'vendor/js/underscore.js',
            'vendor/js/jquery.cookie.js',
            'vendor/js/jquery.simplemodal-1.4.3.js',
            'vendor/js/jquery.endless-scroll.js',
            'vendor/js/moment.js',
            'vendor/js/jquery.grumble.min.js',
            'vendor/js/jquery.crumble.min.js',
            'vendor/js/jquery.easing.1.3.js',
            'vendor/js/jquery.slideviewer.1.2.js',
            'vendor/js/heatmap.js',
            'vendor/js/heatmap-leaflet.js',
            'vendor/js/L.Control.Zoomslider.js',
            'vendor/js/leaflet_numbered_markers.js',
            'vendor/js/require.js',
            'vendor/js/point-in-polygon.js',
            'js/cookie-reader.js',
            'js/*.js',
            'js/posts/*.js',
        ),
        'output_filename': 'js/app.js',
        'variant': 'datauri',
    }
}

POSTMARK_TEST_MODE = False
MEDIA_DEV_MODE = False

# Only send cookies over HTTPS in production
SESSION_COOKIE_SECURE = False

ADMINS = (
    ('Jon Wong', 'j@jnwng.com'),
    ('Lewis Chung', 'lewis.f.chung@gmail.com'),
    ('Wes Vetter', 'wes.vetter@gmail.com'),
)

MANAGERS = ADMINS

# Celery message broker options
BROKER_URL = os.getenv('MYREDIS_URL')
BROKER_BACKEND = 'redis'
CELERY_RESULT_BACKEND = os.getenv('MYREDIS_URL')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://elasticsearch.wehave-weneed.org:9200/',
        'INDEX_NAME': 'haystack',
    },
}

import os
import urlparse

redis_url = urlparse.urlparse(os.environ.get('MYREDIS_URL', 'redis://localhost:6379'))

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': redis_url.password,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        }
    }
}

# Storage
STATICFILES_STORAGE = "whwn.storage.PipelineRequiresStorage"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'WARNING',  # Or maybe INFO or DEBUG
            'propagate': False,
        }
    },
}

SECRET_KEY = os.getenv('WHWN_SECRET_KEY')
