# Generated by Django 3.0.4 on 2020-03-21 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Category name')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Institution name')),
                ('description', models.TextField(max_length=256)),
                ('type', models.IntegerField(choices=[(0, 'fundacja'), (1, 'organizacja pozarządowa'), (2, 'zbiórka lokalna')], default=0)),
                ('categories', models.ManyToManyField(to='donation.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=16)),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=12)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField(max_length=256)),
                ('categories', models.ManyToManyField(to='donation.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation.Institution')),
            ],
        ),
    ]
