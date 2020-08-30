# Generated by Django 3.1 on 2020-08-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amyra', '0004_auto_20200826_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.ImageField(upload_to='drive/pdf')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ('-created',)},
        ),
    ]