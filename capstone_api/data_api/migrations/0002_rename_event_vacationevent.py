# Generated by Django 4.0.5 on 2022-06-28 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='VacationEvent',
        ),
    ]