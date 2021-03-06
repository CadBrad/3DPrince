"""
Django settings for allauthdemo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!h8#n5wopc#7zq!_)i=l#t=q)7g0g-+&0!=kxv+*&2b7*xb8bm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap3', # optional module for making bootstrap forms easier

    'allauth',
    'allauth.account',
    'allauth.socialaccount',


    'allauthdemo.auth',
    'allauthdemo.demo',

    # Social Media uploads
    
    #'allauth.socialaccount.providers.amazon',
    #'allauth.socialaccount.providers.angellist',
    #'allauth.socialaccount.providers.baidu',
    #'allauth.socialaccount.providers.paypal',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.facebook',
    
    #'allauth.socialaccount.providers.asana',
    #'allauth.socialaccount.providers.basecamp',
    #'allauth.socialaccount.providers.battlenet',
    #'allauth.socialaccount.providers.bitbucket',
    #'allauth.socialaccount.providers.bitly',
    #'allauth.socialaccount.providers.coinbase',
    #'allauth.socialaccount.providers.douban',
    #'allauth.socialaccount.providers.digitalocean',
    #'allauth.socialaccount.providers.draugiem',
    #'allauth.socialaccount.providers.dropbox',
    #'allauth.socialaccount.providers.dropbox_oauth2',
    #'allauth.socialaccount.providers.edmodo',
    #'allauth.socialaccount.providers.eveonline',
    #'allauth.socialaccount.providers.evernote',
    #'allauth.socialaccount.providers.feedly',
    #'allauth.socialaccount.providers.flickr',
    #'allauth.socialaccount.providers.foursquare',
    #'allauth.socialaccount.providers.gitlab',
    #'allauth.socialaccount.providers.hubic',
    #'allauth.socialaccount.providers.instagram',
    #'allauth.socialaccount.providers.linkedin',
    #'allauth.socialaccount.providers.linkedin_oauth2',
    #'allauth.socialaccount.providers.mailru',
    #'allauth.socialaccount.providers.windowslive',
    #'allauth.socialaccount.providers.odnoklassniki',
    #'allauth.socialaccount.providers.openid',
    #'allauth.socialaccount.providers.orcid',
    #'allauth.socialaccount.providers.persona',
    #'allauth.socialaccount.providers.pinterest',
    #'allauth.socialaccount.providers.reddit',
    #'allauth.socialaccount.providers.robinhood',
    #'allauth.socialaccount.providers.shopify',
    #'allauth.socialaccount.providers.slack',
    #'allauth.socialaccount.providers.soundcloud',
    #'allauth.socialaccount.providers.spotify',
    #'allauth.socialaccount.providers.stackexchange',
    #'allauth.socialaccount.providers.stripe',
    #'allauth.socialaccount.providers.tumblr',
    #'allauth.socialaccount.providers.twentythreeandme',
    #'allauth.socialaccount.providers.twitch',
    #'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.untappd',
    #'allauth.socialaccount.providers.vimeo',
    #'allauth.socialaccount.providers.weibo',
    #'allauth.socialaccount.providers.weixin',
    #'allauth.socialaccount.providers.vk',
    #'allauth.socialaccount.providers.xing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'allauthdemo.urls'

WSGI_APPLICATION = 'allauthdemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media', 'uploads')

# Authentication

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

TEMPLATES = [
    {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        # allauth templates: you could copy this directory into your
        # project and tweak it according to your needs
        # os.path.join(PROJECT_ROOT, 'templates', 'uniform', 'allauth'),
        # example project specific templates
        os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'plain', 'example'),
        #os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'bootstrap', 'allauth'),
        os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'allauth'),
        os.path.join(BASE_DIR, 'allauthdemo', 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            # needed for admin templates
            'django.contrib.auth.context_processors.auth',
            # these *may* not be needed
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.contrib.messages.context_processors.messages',
            # allauth needs this from django
            'django.template.context_processors.request',
            # allauth specific context processors
            #'allauth.account.context_processors.account',
            #'allauth.socialaccount.context_processors.socialaccount',
          ],
       },
    }
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS =      { 'google':
        { 'SCOPE': ['email'],
          'AUTH_PARAMS': { 'access_type': 'online' }
        }
      }

SITE_ID = 1
AUTH_USER_MODEL = 'allauthdemo_auth.DemoUser'
LOGIN_REDIRECT_URL = '/member/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # testing...
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
SOCIALACCOUNT_AUTO_SIGNUP = False  # require social accounts to use the signup form ... I think
# For custom sign-up form:
# http://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth

