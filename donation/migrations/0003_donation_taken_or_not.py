# Generated by Django 3.0.4 on 2020-03-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_donation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='taken_or_not',
            field=models.BooleanField(default=False),
        ),
    ]