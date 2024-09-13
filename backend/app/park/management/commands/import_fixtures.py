import os

from django.apps import apps
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load data for Park app from fixtures"

    def handle(self, *args, **options):
        # Define the input directory for the fixtures
        input_dir = os.path.join(settings.BASE_DIR, "park", "fixtures")

        # Define the models to load
        models = [
            "park.Park",
            "park.Feature",
            "park.Facility",
            "park.Feedback",
            "park.Photo",
        ]

        # Load data for each model
        for model in models:
            apps.get_model(*model.split(".")).objects.all().delete()

            input_file = os.path.join(input_dir, f'{model.replace(".", "_")}.json')
            if os.path.exists(input_file):
                call_command("loaddata", input_file)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Fixture file {input_file} does not exist")
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully loaded data for Contract models")
        )
