"""
Django settings for CMDBase default website.
"""
import os
import socket
from django.contrib.messages import constants as messages
from cmdbase_utils.settings import CONFIG
from zut import _UNSET, get_logging_dict_config, to_bool


# Security
# WARNING: don't run with debug turned on in production!
# WARNING: keep the secret key used in production secret!
DEBUG = to_bool(os.environ.get('DEBUG', False))

if DEBUG:
    SECRET_KEY = CONFIG.getsecret('cmdbase-site', 'secret_key', fallback='django-insecure-0&&+68@+29bbkyp$xrkfs*cr4u)(4@a#huy=cxif0=u$uw(^5x')
else:
    SECRET_KEY = CONFIG.getsecret('cmdbase-site', 'secret_key')
    ALLOWED_HOSTS = CONFIG.getlist('cmdbase-site', 'allowed_hosts')
    CSRF_TRUSTED_ORIGINS = [f'https://{_host}' for _host in ALLOWED_HOSTS]
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True


# Main definitions

WITH_DEBUG_TOOLBAR = False
if DEBUG:
    try:
        import debug_toolbar
        WITH_DEBUG_TOOLBAR = True
    except ModuleNotFoundError:
        pass

WITH_IMPORT_EXPORT = False
try:
    import import_export
    WITH_IMPORT_EXPORT = True
except ModuleNotFoundError:
    pass


INSTALLED_APPS = []

if WITH_DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')

if WITH_IMPORT_EXPORT:
    INSTALLED_APPS.append('import_export')

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'django_js_choices',
    'cmdbase',
]


MIDDLEWARE = []

if WITH_DEBUG_TOOLBAR:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    
MIDDLEWARE += [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cmdbase.middleware.CMDBaseMiddleware'
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cmdbase.context_processors.cmdbase',
            ],
        },
    },
]

ROOT_URLCONF = 'cmdbase.site.urls'

WSGI_APPLICATION = 'cmdbase.site.wsgi.application'

if WITH_DEBUG_TOOLBAR:
    INTERNAL_IPS = [
        '127.0.0.1', # Localhost
        '10.0.2.2',  # Virtualbox host
    ]
    
    # Docker
    _, _, ips = socket.gethostbyname_ex(socket.gethostname())
    for ip in ips:
        internal_ip = ip[:ip.rfind(".")] + ".1"
        if not internal_ip in INTERNAL_IPS:
            INTERNAL_IPS.append(internal_ip)


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONFIG.get('cmdbase-site', 'db_name', fallback='cmdbase'),
        'USER': CONFIG.get('cmdbase-site', 'db_user', fallback='postgres'),
        'PASSWORD': CONFIG.getsecret('cmdbase-site', 'db_password', fallback=None),
        'HOST': CONFIG.get('cmdbase-site', 'db_host', fallback=None),
        'PORT': CONFIG.getint('cmdbase-site', 'db_port', fallback=None),
        "TEST": {
            "CHARSET": 'UTF-8',
        },
    }
}


# Authentication
# https://docs.djangoproject.com/fr/4.2/topics/auth/customizing/#substituting-a-custom-user-model
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
# https://docs.djangoproject.com/en/4.2/ref/settings/#login-url

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = 'admin:login'
LOGIN_REDIRECT_URL = 'cmdbase:index'

LOGOUT_URL = 'admin:logout'
LOGOUT_REDIRECT_URL = 'cmdbase:index'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'
USE_I18N = True

TIME_ZONE = 'Europe/Malta'
USE_TZ = True

LANGUAGES = [
    ('en', "English"),
    ('fr', "French"),
    ('ru', "Russian"),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATIC_ROOT = CONFIG.get('cmdbase-site', 'static_root', fallback='local/static' if DEBUG else _UNSET)  # target directory for "collectstatic" command (used only in production)
MEDIA_ROOT = CONFIG.get('cmdbase-site', 'media_root', fallback='local/media' if DEBUG else _UNSET)     # application-related media

LOCAL_STATIC_LIB = CONFIG.getboolean('cmdbase-site', 'local_static_lib', fallback=False) # Used by static_lib template tags.


# Messages framework: use Bootstrap colors
# https://docs.djangoproject.com/en/4.1/ref/contrib/messages/

MESSAGE_TAGS = {
    # Bootstrap colors
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Logging
# See https://docs.djangoproject.com/en/4.2/ref/settings/#logging

LOGGING = get_logging_dict_config()
