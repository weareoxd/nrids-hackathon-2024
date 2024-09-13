from .base import Base


class Test(Base):

    """
    Application settings for automated tests.
    """

    # Test in memory for speed and portability
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }
