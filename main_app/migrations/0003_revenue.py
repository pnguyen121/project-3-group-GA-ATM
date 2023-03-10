# Generated by Django 4.1.4 on 2023-01-06 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_location_type_atm_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('yearly', models.IntegerField()),
                ('atm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.atm')),
            ],
        ),
    ]
