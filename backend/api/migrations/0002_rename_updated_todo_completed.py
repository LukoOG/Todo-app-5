# Generated by Django 5.2 on 2025-05-07 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='updated',
            new_name='completed',
        ),
    ]
