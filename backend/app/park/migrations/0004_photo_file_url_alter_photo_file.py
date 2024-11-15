# Generated by Django 5.1.1 on 2024-09-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("park", "0003_alter_facility_facility_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="file_url",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="photo",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="photos/"),
        ),
    ]
