# Generated by Django 2.2 on 2020-08-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amyra', '0008_calculation_cgst'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='igst',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
