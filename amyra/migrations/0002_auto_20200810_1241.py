# Generated by Django 2.2 on 2020-08-10 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amyra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='destination',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='amyra.Destination'),
        ),
    ]
