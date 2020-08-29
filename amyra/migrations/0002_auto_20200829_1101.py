# Generated by Django 3.1 on 2020-08-29 05:16

import amyra.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amyra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='description',
        ),
        migrations.RemoveField(
            model_name='file',
            name='location',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=amyra.models.file_location_path, verbose_name='File'),
        ),
    ]
