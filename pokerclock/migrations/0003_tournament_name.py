# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerclock', '0002_auto_20160314_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='name',
            field=models.CharField(default='New Tournament', max_length=200),
        ),
    ]
