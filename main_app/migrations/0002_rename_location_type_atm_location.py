# Generated by Django 4.1.4 on 2023-01-05 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atm',
            old_name='location_type',
            new_name='location',
        ),
    ]
