# Generated by Django 5.1 on 2024-09-19 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
