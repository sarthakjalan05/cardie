# Generated by Django 5.0.3 on 2024-04-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_server_production'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='production',
            field=models.BooleanField(default=0),
        ),
    ]