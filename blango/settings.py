"""
Class-based Django settings using django-configurations.
"""

from pathlib import Path
import os
import dj_database_url
from configurations import Configuration, values


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class Common(Configuration):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-+sn%dpa!086+g+%44z9*^j^q-u4n!j(#wl)x9a%_1op@zz2+1-'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue(["127.0.0.1", "localhost", "0.0.0.0", ".codio.io"])

    # Configure frame options and CSRF origins safely depending on environment
    CODIO_HOSTNAME = os.environ.get('CODIO_HOSTNAME')

    # Django 3.2 no longer supports 'ALLOW-FROM'; default to SAMEORIGIN
    X_FRAME_OPTIONS = 'SAMEORIGIN'

    # CSRF settings
    CSRF_COOKIE_SAMESITE = None
    if CODIO_HOSTNAME:
        CSRF_TRUSTED_ORIGINS = [f'https://{CODIO_HOSTNAME}-8000.codio.io']
    else:
        CSRF_TRUSTED_ORIGINS = []

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SAMESITE = 'None'

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'crispy_forms',
        'blog',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        #'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'blango.urls'

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

    WSGI_APPLICATION = 'blango.wsgi.application'

    # Database: single SQLite database for this project
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    # Password validation
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
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = values.Value("UTC")
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'

    # Default primary key field type
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # django-crispy-forms settings
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
    CRISPY_TEMPLATE_PACK = "bootstrap4"


class Development(Common):
    DEBUG = True
    # Allow all hosts in development to avoid DisallowedHost
    ALLOWED_HOSTS = ["*"]


class Production(Common):
    DEBUG = False
    # Require SECRET_KEY via environment in production
    SECRET_KEY = values.SecretValue()
    # Security hardening
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_HSTS_PRELOAD = values.BooleanValue(True)
    # Optionally override CSRF trusted origins via env
    CSRF_TRUSTED_ORIGINS = values.ListValue(default=[])
