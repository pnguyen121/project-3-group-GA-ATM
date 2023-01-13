# Generated by Django 4.1.2 on 2023-01-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='atm',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='atm',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atm',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]