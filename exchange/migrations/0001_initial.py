# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-12 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=100)),
                ('c_code', models.CharField(max_length=50)),
            ],
        ),
    ]
