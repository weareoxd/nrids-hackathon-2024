# Generated by Django 5.1.1 on 2024-09-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("park", "0004_photo_file_url_alter_photo_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="facility",
            field=models.CharField(max_length=255),
        ),
    ]
