# Generated by Django 4.1.4 on 2023-01-06 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_revenue_yearly'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenue',
            options={'ordering': ['-date']},
        ),
    ]
