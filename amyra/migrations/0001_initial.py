# Generated by Django 2.0 on 2020-08-10 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField(blank=True, null=True)),
                ('sgst', models.IntegerField(blank=True, null=True)),
                ('cgst', models.IntegerField(blank=True, null=True)),
                ('igst', models.IntegerField(blank=True, null=True)),
                ('total_amount_after_tax', models.IntegerField(blank=True, null=True)),
                ('total_amount_in_words', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField()),
                ('city', models.CharField(max_length=12)),
                ('state', models.CharField(max_length=15)),
                ('gst_no', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True)),
                ('bill_type', models.CharField(max_length=500, null=True)),
                ('invoice_no', models.CharField(max_length=500, null=True)),
                ('hsn_code', models.CharField(max_length=4)),
                ('dated', models.DateField()),
                ('transport', models.CharField(max_length=500, null=True)),
                ('vehicle_no', models.CharField(max_length=500, null=True)),
                ('challan_no', models.CharField(max_length=500, null=True)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amyra.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('design_name', models.CharField(max_length=500)),
                ('qty', models.IntegerField()),
                ('dibbi', models.IntegerField(choices=[(6, '6 dibbi'), (12, '12 dibbi')], default=12)),
                ('pics', models.IntegerField(blank=True, editable=False, null=True)),
                ('rate', models.IntegerField()),
                ('amount', models.IntegerField(blank=True, editable=False, null=True)),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='amyra.Destination')),
            ],
        ),
        migrations.AddField(
            model_name='calculation',
            name='destination',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='amyra.Destination'),
        ),
    ]
