# Generated by Django 3.1 on 2020-08-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amyra', '0003_files_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='file',
            field=models.ImageField(upload_to='drive/images'),
        ),
    ]
