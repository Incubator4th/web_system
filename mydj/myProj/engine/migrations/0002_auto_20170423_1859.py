# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-23 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reportid',
            field=models.CharField(db_column='Report_ID', default='', max_length=10, primary_key=True, serialize=False),
        ),
    ]
