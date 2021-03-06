"""
Django settings for wikilegis project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))

# Import `default` as the default settings. This can be handy while pushing items into tuples.
import django.conf.global_settings as default


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g8#!8*0sr!zsg!q=on=n66dtie69u0z1qhfk-&c8bc_%t#&g@%'

API_KEY = config('API_KEY', default='9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'wikilegis.auth2',
    'wikilegis.core',
    'wikilegis.comments2',
    'wikilegis.notification',
    'flat',
    'object_tools',
    'export',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    'haystack',
    'compressor',
    'adminsortable2',
    'debug_toolbar',
    'registration',
    'django_comments',
    'django_extensions',
    'rules.apps.AutodiscoverRulesConfig',
    'embed_video',
    'social.apps.django_app.default',
    'easy_thumbnails',
    'image_cropping',
    'rest_framework',
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.AllowAny',
    ],
    'PAGE_SIZE': 10
}

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'wikilegis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'wikilegis', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wikilegis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# django-haystack: http://django-haystack.readthedocs.org/
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}


LOCALE_PATHS = [
    os.path.join(HERE, 'locale'),
]


# Authentication and user management

AUTH_USER_MODEL = 'auth2.User'

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.Facebook2OAuth2',
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# If `False` the registration view will not require user activation through e-mail.
# Useful to disable activation during DEBUG or other situations where mails can't be sent.
ACCOUNT_ACTIVATION_REQUIRED = not DEBUG

ACCOUNT_ACTIVATION_DAYS = 7

REGISTRATION_AUTO_LOGIN = True

REGISTRATION_FORM = 'wikilegis.auth2.forms.RegistrationForm'

# XXX Please don't change. The URL is included in `wikilegis.auth2.urls`.
INCLUDE_REGISTER_URL = False


# python-social-auth: http://psa.matiasaguirre.net/docs/index.html

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

# We just want the *social user*'s email. Not the username.
# This is used by `social.pipeline.user.create_user` to create the user.
# Since our user has no username, we have to remove it from the list.
USER_FIELDS = ('email',)


# Fill these with your application credentials in order to use social logins.

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,first_name,last_name,email'
}


# Information about available social backends. I know this is not the
# best place to put this kind of things, but what could one do?

SOCIAL_BACKEND_INFO = {
    'google-oauth2': {
        'title': _('Google'),
        'icon': 'img/sa-google-icon.png',
    },
    'facebook': {
        'title': _('Facebook'),
        'icon': 'img/sa-facebook-icon.png',
    }
}


# Site-specific settings

SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

languages = dict(default.LANGUAGES)
language_tuple = lambda language_code: (language_code, languages[language_code])

LANGUAGES = (
    language_tuple('en'),
    language_tuple('pt-br'),
)

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'public', 'static'))

STATICFILES_FINDERS = default.STATICFILES_FINDERS + (
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'wikilegis', 'static'),
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

LIBSASS_SOURCEMAPS = DEBUG

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'public', 'media'))

## Debug toolbar
STATIC_IPS = ('127.0.0.1', '::1', )

# Login settings
LOGIN_REDIRECT_URL = '/'

SERIALIZATION_MODULES = {
    'csv': 'export.serializers.csv_serializer'
}

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
