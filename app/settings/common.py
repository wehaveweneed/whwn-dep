# Django settings for whwn project.
import os
import sys
import json

def project(*args):
    path = os.path.join(os.path.dirname(__file__), "../")
    file_path = os.path.realpath(path)
    return os.path.join(file_path, *args)

ADMINS = (
    ('WeHave-WeNeed', 'admin@wehave-weneed.org'),
)

# Celery
import djcelery
djcelery.setup_loader()

CELERY_QUEUES = {
    'default': {
        'exchange': 'default',
        'exchange_type': 'topic',
        'binding_key': 'tasks.#',
    }
}
CELERY_DEFAULT_QUEUE = "default"
CELERY_IMPORTS = ("whwn.tasks",)

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Registration options
ACCOUNT_ACTIVATION_DAYS = 7

MANAGERS = ADMINS

DATETIME_FORMAT = "U"

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = False

# Custom WHWN Authentication Backend. Look at
# whwn/auth_backends.py for more information.
AUTHENTICATION_BACKENDS = (
   'whwn.auth_backends.WHWNUserAuthBackend',
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_DOC_ROOT = 'home/site-directory/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

PIPELINE_COMPASS_ARGUMENTS = '-c %s' % project('static/config.rb')
PIPELINE_COMPILERS = ('pipeline_compass.compass.CompassCompiler',)
PIPELINE_CSS = {
    'app': {
        'source_filenames': (
            'vendor/jqueryUI/css/smoothness/jquery-ui-1.10.0.custom.css',
            'vendor/css/crumble.css',
            'vendor/css/grumble.min.css',
            'vendor/css/slideviewer.css',
            'vendor/css/L.Control.Zoomslider.css',
            'vendor/css/leaflet_numbered_markers.css',
            'vendor/css/backgrid.css',
            'vendor/css/backgrid-select2-cell.css',
            'vendor/css/select2.css',
            'sass/base.sass',
        ),
        'output_filename': '.css/app.css',
        'variant': 'datauri',
    },
}

# RequireJS options
REQUIRE_BASE_URL = "coffee/backbone"
REQUIRE_ENVIRONMENT = "node"
REQUIRE_JS = "components/requirejs/require.js"
REQUIRE_BUILD_PROFILE = "../app.inventory.js"
REQUIRE_STANDALONE_MODULES = {
    "main": {
        "out": "inventory-built.js",
        "build_profile": "../app.inventory.js",
    }
}

STATICFILES_DIRS = (
    project('static/'),
    project('tools/static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Fixtures for initial data
FIXTURES_DIR = (
    project("fixtures/"),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.contrib.messages.context_processors.messages'
)

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # Timeout Middleware is used to time out someones session after a specified period of time
    # 'middleware.timeoutmiddleware.TimeoutMiddleware',

    'pipeline.middleware.MinifyHTMLMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', 
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.gis',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_jenkins',
    'haystack',
    'adminplus',
    'debug_toolbar',
    'django_extensions',
    # in conjunction with django.contrib.staticfiles
    'pipeline',
    'whwn',
    'whwn.templatetags',
    'tools',
    'registration',
    'postmark',
    'south',
    'djcelery',
    'tastypie',
    'require',
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

def custom_show_toolbar(request):
    return True # Always show toolbar, for example purposes only.

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': None,
    'EXTRA_SIGNALS': [],
    'HIDE_DJANGO_SQL': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'TAG': 'body',
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    project("templates/"),
    project('tools/templates/'),
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # },
    }
}

TEST_RUNNER = 'whwn.testing.WhwnTestSuiteRunner'

AUTH_PROFILE_MODULE = 'whwn.UserProfile'

LOGIN_URL = '/accounts/login/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
