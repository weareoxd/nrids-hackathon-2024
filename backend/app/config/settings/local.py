import socket

from configurations.values import BooleanValue, Value

from .base import Base


class Local(Base):
    """
    Application settings for local development.
    """

    CORS_ALLOWED_ORIGIN_REGEXES = Base.CORS_ALLOWED_ORIGIN_REGEXES + [
        r"^http:\/\/(localhost|(127\.0\.0\.1))(:(8080|5173))?$"
    ]

    THIRD_PARTY_APPS = Base.THIRD_PARTY_APPS + ["django_extensions"]

    QUERYCOUNT = {
        "THRESHOLDS": {
            "MEDIUM": 50,
            "HIGH": 200,
            "MIN_TIME_TO_LOG": 0,
            "MIN_QUERY_COUNT_TO_LOG": 0,
        },
        "IGNORE_REQUEST_PATTERNS": [r"^/admin/"],
        "IGNORE_SQL_PATTERNS": [],
        "DISPLAY_DUPLICATES": None,
        "RESPONSE_HEADER": "X-DjangoQueryCount-Count",
    }

    INTERNAL_IPS = ["127.0.0.1"]

    # Discover our internal id inside the docker container
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

    USE_DJANGO_DEBUG_TOOLBAR = BooleanValue(
        False,
        environ_prefix=None,
    )

    THIRD_PARTY_APPS = Base.THIRD_PARTY_APPS + [
        "drf_yasg",
    ]

    MIDDLEWARE = Base.MIDDLEWARE + [
        "querycount.middleware.QueryCountMiddleware",
    ]

    @classmethod
    def setup(cls):
        super().setup()

        # Set logging to dev console
        cls.LOGGING = Base.LOGGING.copy()
        cls.LOGGING["handlers"]["console"]["formatter"] = "dev_console"

        # some dev libraries are are very noisy at DEBUG
        cls.LOGGING["loggers"]["faker"] = {
            "handlers": ["console"],
            "level": Value("WARNING", environ_name="FAKER_LOG_LEVEL"),
            "propagate": False,
        }
        cls.LOGGING["loggers"]["factory"] = {
            "handlers": ["console"],
            "level": Value("WARNING", environ_name="FACTORY_LOG_LEVEL"),
            "propagate": False,
        }
        cls.LOGGING["loggers"]["watchdog"] = {
            "handlers": ["console"],
            "level": Value("INFO", environ_name="WATCHDOG_LOG_LEVEL"),
            "propagate": False,
        }
        cls.LOGGING["loggers"]["django_structlog.middlewares.request"] = {
            "handlers": ["console"],
            "level": Value("WARNING", environ_name="REQUEST_LOG_LEVEL"),
            "propagate": False,
        }

        if cls.USE_DJANGO_DEBUG_TOOLBAR:
            cls.THIRD_PARTY_APPS.append("debug_toolbar")

            cls.MIDDLEWARE = [
                "debug_toolbar.middleware.DebugToolbarMiddleware",
            ] + cls.MIDDLEWARE
