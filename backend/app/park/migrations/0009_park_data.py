# Generated by Django 5.1.1 on 2024-09-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("park", "0008_park_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="park",
            name="data",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
