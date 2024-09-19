import json
import os
from io import StringIO

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Dump data for Park app to a fixture"

    def handle(self, *args, **options):
        # Define the output directory for the fixtures
        output_dir = os.path.join(settings.BASE_DIR, "park", "fixtures")
        os.makedirs(output_dir, exist_ok=True)

        # Define the models to dump
        models = [
            "park.Park",
            "park.Feature",
            "park.Facility",
            "park.Feedback",
            "park.Photo",
        ]

        # Dump data for each model
        for model in models:
            output_file = os.path.join(output_dir, f'{model.replace(".", "_")}.json')
            with open(output_file, "w") as f:
                # Use StringIO to capture the output of dumpdata
                out = StringIO()
                call_command("dumpdata", model, stdout=out)
                # Load the JSON data
                data = json.loads(out.getvalue())
                # Dump the JSON data with indentation
                json.dump(data, f, indent=4)

        self.stdout.write(
            self.style.SUCCESS("Successfully dumped data for Park models")
        )
