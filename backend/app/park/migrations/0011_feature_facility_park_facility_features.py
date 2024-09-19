# Generated by Django 5.1.1 on 2024-09-19 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0010_remove_park_image_remove_park_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='park',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facilities', to='park.park'),
        ),
        migrations.AddField(
            model_name='facility',
            name='features',
            field=models.ManyToManyField(related_name='facilities', to='park.feature'),
        ),
    ]