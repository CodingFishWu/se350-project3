# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_traderserver_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='code',
            field=models.CharField(default='', max_length=20),
        ),
    ]
