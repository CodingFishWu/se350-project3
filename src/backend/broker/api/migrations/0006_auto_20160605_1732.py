# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160601_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraderServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('credits', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(default='trade', max_length=10),
        ),
    ]
