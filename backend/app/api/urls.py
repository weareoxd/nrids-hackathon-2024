import os

from django.conf import settings
from django.urls import path

# from .contract import urls as contract_urls
from .views import HealthCheck

urlpatterns = [
    path("health-check", HealthCheck.as_view(), name="health-check"),
    # path("view/", include((view_urls, "view"))),
]


if os.environ["DJANGO_CONFIGURATION"] != "Production":
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view as swagger_get_schema_view

    urlpatterns.append(
        path(
            "swagger",
            swagger_get_schema_view(
                openapi.Info(
                    title=f"{settings.SITE_NAME} API",
                    default_version=f"{settings.SITE_VERSION}",
                    description=f"{settings.SITE_NAME} internal APIs",
                ),
                public=True,
            ).with_ui("swagger", cache_timeout=0),
            name="swagger-schema",
        ),
    )
