# Generated by Django 2.0 on 2020-08-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amyra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='transport_cost',
            field=models.CharField(max_length=500, null=True),
        ),
    ]