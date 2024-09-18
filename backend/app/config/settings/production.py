import httpx
from configurations.values import Value

from .base import Base


class Production(Base):

    """
    Production application settings.

    Most settings should go in base instead; we don't want settings
    in production that we're not running in dev, if we can help it.
    """

    STATIC_ROOT = "/var/www/html/static"

    # S3 bucket settings
    THIRD_PARTY_APPS = Base.THIRD_PARTY_APPS + ["storages"]  # noqa: F841

    AWS_ACCESS_KEY_ID = Value(  # noqa: F841
        "",
        environ_prefix=None,
    )
    AWS_SECRET_ACCESS_KEY = Value(  # noqa: F841
        "",
        environ_prefix=None,
    )
    AWS_STORAGE_BUCKET_NAME = Value(
        "",
        environ_prefix=None,
    )
    AWS_S3_REGION_NAME = Value(  # noqa: F841
        "ca-central-1",
        environ_prefix=None,
    )
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # For serving static files directly from S3
    AWS_S3_URL_PROTOCOL = "https"
    AWS_S3_USE_SSL = True  # noqa: F841
    AWS_S3_VERIFY = True  # noqa: F841

    # Static and media file configuration
    # STATIC_URL = f"{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/static/"  # noqa: F841
    MEDIA_URL = f"{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/media/"  # noqa: F841

    STORAGES = {
        "default": {"BACKEND": "app.config.storage.PublicMediaStorage"},
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
        },
    }

    @classmethod
    def setup(cls):
        super().setup()

        # Get the IMDSv2 token
        IMDSv2_TOKEN = httpx.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "3600"},
        ).text

        # Get the EC2 private IP using the token
        EC2_PRIVATE_IP = httpx.get(
            "http://169.254.169.254/latest/meta-data/local-ipv4",
            headers={"X-aws-ec2-metadata-token": IMDSv2_TOKEN},
        ).text

        # Add the EC2 private IP
        print(f"Adding EC2 private IP {EC2_PRIVATE_IP} to ALLOWED_HOSTS")
        cls.ALLOWED_HOSTS.append(EC2_PRIVATE_IP)
        print(f"ALLOWED_HOSTS: {cls.ALLOWED_HOSTS}")
