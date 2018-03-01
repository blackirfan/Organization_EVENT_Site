# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 04:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('established', models.CharField(max_length=250)),
                ('organization_name', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('organization_logo', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Special_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=500)),
                ('time', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=20000)),
                ('location', models.CharField(max_length=500)),
                ('event_detail', models.CharField(max_length=500)),
                ('is_favorite', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Organization')),
            ],
        ),
    ]