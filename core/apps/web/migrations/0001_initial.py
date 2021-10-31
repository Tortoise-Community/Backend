# Generated by Django 3.2.8 on 2021-10-31 15:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True, blank=True, unique=True)),
                ('name', models.CharField(max_length=15)),
                ('prize', models.CharField(max_length=150)),
                ('host', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=300)),
                ('long_desc', models.TextField()),
                ('event_type', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), help_text='You can add 5 labels (max)', size=5)),
                ('style', models.CharField(choices=[('default.min.css', 'Default'), ('dark.min.css', 'Dark'), ('dracula.min.css', 'Dracula'), ('tomorrow.min.css', 'Tomorrow'), ('night-owl.min.css', 'Night Owl'), ('codepen-embed.min.css', 'Codepen'), ('github-gist.min.css', 'Github Gist'), ('atom-one-dark.min.css', 'Atom Dark'), ('solarized-dark.min.css', 'Solarized Dark'), ('atelier-cave-dark.min.css', 'Atelier Cave'), ('tomorrow-night-blue.css', 'Tomorrow Night Blue'), ('atom-one-dark-reasonable.min.css', 'Atom Dark Reasonable')], default='default.min.css', max_length=50)),
                ('due_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True, blank=True, unique=True)),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=200)),
                ('brief', models.TextField()),
                ('github', models.URLField(blank=True)),
                ('commits', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('stars', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('forks', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('contributors', models.PositiveSmallIntegerField(blank=True, default=0)),
            ],
        ),
    ]
