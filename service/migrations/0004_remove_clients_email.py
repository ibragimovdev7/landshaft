# Generated by Django 4.0.2 on 2022-03-18 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_clients_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='email',
        ),
    ]