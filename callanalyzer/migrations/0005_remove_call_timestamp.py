# Generated by Django 3.0.2 on 2020-01-08 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callanalyzer', '0004_call_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='call',
            name='timestamp',
        ),
    ]
