"""
Project settings.

Settings are split by env using
[django-configurations](https://github.com/jazzband/django-configurations).

Each env (Local, Test, Production) is a class inheriting from Base settings.
Most settings should be put in Base.

To read a setting from the environment, use a `Value`. e.g.:
```
    LANGUAGE_CODE = Value("en-ca")
```
will use the value of DJANGO_LANGUAGE_CODE from the environment if set,
otherwise will use `en-ca`. For more details, see:
https://django-configurations.readthedocs.io/en/stable/values/
"""

from .local import Local
from .production import Production
from .test import Test

__all__ = ("Local", "Test", "Production")
