# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-06 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='realname',
            field=models.CharField(default='Unknown', max_length=10, verbose_name='Name'),
        ),
    ]