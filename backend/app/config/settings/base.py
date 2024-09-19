"""
Base application settings

`Value` settings are exposed via env vars.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

import structlog
from configurations import Configuration
from configurations.values import BooleanValue, IntegerValue, ListValue, Value

from ..logging import configure_structlog, fluentd_json, timestamper


class Base(Configuration):

    # Site name
    # Used in the Django admin header and title
    SITE_NAME = Value(
        "Django",
        environ_prefix=None,
    )

    SITE_VERSION = Value(
        "1.0",
        environ_prefix=None,
    )

    BASE_URL = Value("http://localhost:8000", environ_prefix=None)

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = Value(
        "django-insecure-$ht2gpofbq6!=fqzg$)%p%@8#fxv*3defhyvuhahizx3b^_@e9",
        environ_prefix=None,
    )

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = BooleanValue(False, environ_name="DEBUG", environ_prefix=None)

    ALLOWED_HOSTS = ListValue(
        ["localhost"],
        separator=" ",
        environ_prefix=None,
    )
    CSRF_TRUSTED_ORIGINS = ListValue(
        ["http://localhost"],
        separator=" ",
        environ_prefix=None,
    )
    CORS_ALLOW_ALL_ORIGINS = True
    # CORS_ALLOWED_ORIGIN_REGEXES = []

    # Application definition
    DJANGO_APPS = [
        "django_database_prefix",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    THIRD_PARTY_APPS = [
        "corsheaders",
        "rest_framework",
    ]
    LOCAL_APPS = [
        "app.park.apps.ParkConfig",
    ]

    @property
    def INSTALLED_APPS(self):
        return self.DJANGO_APPS + self.THIRD_PARTY_APPS + self.LOCAL_APPS

    MIDDLEWARE = [
        "django.middleware.gzip.GZipMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "django_structlog.middlewares.RequestMiddleware",
    ]

    ROOT_URLCONF = "app.core.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["app/templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/5.0/ref/settings/#databases
    DB_PREFIX = "nrids_hackathon_db_"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": Value(
                "",
                environ_name="DB_DATABASE",
                environ_prefix=None,
            ),
            "USER": Value(
                "",
                environ_name="DB_USER",
                environ_prefix=None,
            ),
            "PASSWORD": Value(
                "",
                environ_name="DB_PASSWORD",
                environ_prefix=None,
            ),
            "HOST": Value(
                "",
                environ_name="DB_HOST",
                environ_prefix=None,
            ),
            "PORT": IntegerValue(
                5432,
                environ_name="DB_PORT",
                environ_prefix=None,
            ),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: B950 pylint: disable=line-too-long
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/5.0/topics/i18n/
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "America/Vancouver"
    USE_I18N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.0/howto/static-files/
    STATIC_URL = "static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "../static")

    # Uploads
    # https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/
    MEDIA_URL = "media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "../media")
    FILE_UPLOAD_PERMISSIONS = 0o644

    # HTTP
    # https://docs.djangoproject.com/en/5.0/ref/settings/#data-upload-max-number-fields
    DATA_UPLOAD_MAX_NUMBER_FIELDS = None

    # Default primary key field type
    # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    # Account settings
    # AUTH_USER_MODEL = "account.User"

    # Logging
    LOG_DIR = os.path.join(BASE_DIR, "../logs")
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(
                    serializer=fluentd_json,
                ),
                "foreign_pre_chain": [
                    structlog.contextvars.merge_contextvars,
                    timestamper,
                    structlog.stdlib.add_logger_name,
                    structlog.stdlib.add_log_level,
                    structlog.stdlib.PositionalArgumentsFormatter(),
                ],
            },
            "dev_console": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.dev.ConsoleRenderer(),
                "foreign_pre_chain": [
                    structlog.contextvars.merge_contextvars,
                    timestamper,
                    structlog.stdlib.add_logger_name,
                    structlog.stdlib.add_log_level,
                    structlog.stdlib.PositionalArgumentsFormatter(),
                ],
            },
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "json",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": Value("WARNING", environ_name="LOG_LEVEL"),
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": Value("WARNING", environ_name="LOG_LEVEL"),
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": Value("WARNING", environ_name="LOG_LEVEL_DB"),
                "propagate": False,
            },
            "django.template": {
                "handlers": ["console"],
                "level": Value("WARNING", environ_name="LOG_LEVEL_TEMPLATE"),
                "propagate": False,
            },
            "app": {
                "handlers": ["console"],
                "level": Value("INFO", environ_name="LOG_LEVEL_APP"),
                "propagate": False,
            },
        },
    }

    # Django REST Framework settings
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.SessionAuthentication",
            "rest_framework.authentication.BasicAuthentication",
        ],
    }

    @classmethod
    def setup(cls):
        super().setup()

        configure_structlog()
