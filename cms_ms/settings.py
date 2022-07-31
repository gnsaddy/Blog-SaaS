"""
Django settings for cms_ms project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
from os import getenv
import sys

import django

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0l*mm15rczeo%v8k4s2m16ysa-zsam62#$xyt4u)e#(mf#r*kj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost:1337', 'http://3.132.21.77']
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'apps',
    'apps.auths'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cms_ms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cms_ms.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'cms_dev'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'codejeedev2020'),
        'HOST': os.environ.get('MYSQL_DATABASE_HOST', '3.132.21.77'),
        'PORT': os.environ.get('MYSQL_DATABASE_PORT', 3306),
        'default-character-set': 'utf8',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ALLOW_ALL_ORIGINS = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'auths.CustomUser'

# REST Framework Settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'AUTH_COOKIE_SECURE': False,
    'AUTH_COOKIE_HTTP_ONLY': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': 'Bearer',
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=25),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=15),

    # custom
    # Cookie name. Enables cookies if value is set.
    'AUTH_COOKIE': 'access_token',
    # A string like "example.com", or None for standard domain cookie.
    'AUTH_COOKIE_DOMAIN': None,
    # Whether the auth cookies should be secure (https:// only).
    # Http only cookie flag.It's not fetch by javascript.
    # The path of the auth cookie. Whether to set the flag restricting cookie leaks
    'AUTH_COOKIE_PATH': '/',
    # on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag.
    'AUTH_COOKIE_SAMESITE': 'None',
}

# LOGIN_URL = '/login'
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/login'

SPECTACULAR_SETTINGS = {
    'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAuthenticated'],
    # None will default to DRF's AUTHENTICATION_CLASSES
    'SERVE_AUTHENTICATION': ['rest_framework.authentication.BasicAuthentication'],
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        "persistAuthorization": True,
        "displayOperationId": True,
        "defaultModelsExpandDepth": 1,
    },

    'GENERIC_ADDITIONAL_PROPERTIES': 'dict',
    'SORT_OPERATION_PARAMETERS': True,

    # Option for turning off error and warn messages
    'DISABLE_ERRORS_AND_WARNINGS': False,
    'TITLE': 'Codejee CMS API Documentation',
    'DESCRIPTION': 'Codejee CMS API Documentation',
    'TOS': "https://www.google.com/policies/terms/",
    # Optional: MAY contain "name", "url", "email"
    'CONTACT': {
        "name": "Aditya Raj",
        "email": "gnsaddy@gmail.com",
        "url": "https://www.codejee.com/",
    },
    # Optional: MUST contain "name", MAY contain URL
    'LICENSE': {
        "name": "BSD License",
        "url": "https://www.google.com/policies/terms/",
        "terms_of_service": "https://www.google.com/policies/terms/"

    },
    'VERSION': 'V1.1.2',

    'SERVERS': [],
    # Tags defined in the global scope
    'TAGS': [
        {
            'name': 'Codejee CMS',
            'description': 'Codejee CMS API Documentation',
        }
    ],
    # Optional: MUST contain 'url', may contain "description"
    'EXTERNAL_DOCS': {
        'description': 'Codejee CMS API',
        'url': 'https://www.google.com/'
    },
    'EXTENSIONS_INFO': {
        'x-django-version': django.get_version(),
        'x-python-version': sys.version.split('\n')[0],
        'x-framework-version': '{} {}'.format(
            django.VERSION,
            django.get_version()
        ),
        'x-application-name': 'Codejee CMS API',
        'x-application-url': 'https://www.google.com/',
        'x-application-email': 'admin@codejee.com',
        'x-application-author': 'Aditya Raj',
        'x-application-author-email': 'gnsaddy@gmail.com'
    },
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}
