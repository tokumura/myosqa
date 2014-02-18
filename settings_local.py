# encoding:utf-8
import os.path

SITE_SRC_ROOT = os.path.dirname(__file__)
LOG_FILENAME = 'django.osqa.log'
LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
        },
    },
    'loggers' : {
        # ensure that all log entries are propagated to root
        'django': { 'propagate': True },
        'django.request': { 'propagate': True },
        'django.security': { 'propagate': True },
        'py.warnings': { 'propagate': True },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

#ADMINS and MANAGERS
ADMINS = ()
MANAGERS = ADMINS

DEBUG = False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True
}
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = ('*',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'osqa',
        'USER': 'osqa',
        'PASSWORD': 'osqapass',
        'HOST': '',
        'PORT': '',
    }
}

CACHE_BACKEND = 'file://%s' % os.path.join(os.path.dirname(__file__),'cache').replace('\\','/')
#CACHE_BACKEND = 'dummy://'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# This should be equal to your domain name, plus the web application context.
# This shouldn't be followed by a trailing slash.
# I.e., http://www.yoursite.com or http://www.hostedsite.com/yourhostapp
APP_URL = 'http://127.0.0.1'

#LOCALIZATIONS
TIME_ZONE = 'Asia/Tokyo'

#OTHER SETTINGS

USE_I18N = True
LANGUAGE_CODE = 'ja'

DJANGO_VERSION = 1.6
OSQA_DEFAULT_SKIN = 'default'

DISABLED_MODULES = ['books', 'recaptcha', 'project_badges', 'mysqlfulltext']
