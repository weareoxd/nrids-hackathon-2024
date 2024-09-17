import httpx

from .base import Base


class Production(Base):

    """
    Production application settings.

    Most settings should go in base instead; we don't want settings
    in production that we're not running in dev, if we can help it.
    """

    STATIC_ROOT = "/var/www/html/static"

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
