# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160605_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_order_id', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
