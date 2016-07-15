# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_enumfield.db.fields
import yunity.users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('display_name', models.TextField()),
                ('first_name', models.TextField(null=True)),
                ('last_name', models.TextField(null=True)),
                ('profile_visibility', django_enumfield.db.fields.EnumField(default=0, enum=yunity.users.models.ProfileVisibility)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', yunity.users.models.UserManager()),
            ],
        ),
    ]
