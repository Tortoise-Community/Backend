# Generated by Django 3.2.8 on 2021-11-01 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='brief',
            new_name='long_desc',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='short_desc',
        ),
    ]
