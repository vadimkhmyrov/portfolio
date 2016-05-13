# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerclock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='testID',
        ),
        migrations.AddField(
            model_name='tournament',
            name='addon_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournament',
            name='addon_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tournament',
            name='blinds',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tournament',
            name='break_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tournament',
            name='buy_in',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tournament',
            name='knockout_bool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournament',
            name='knockout_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tournament',
            name='level_time',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='tournament',
            name='players',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='tournament',
            name='rebuy_level_stop',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='tournament',
            name='rebuy_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tournament',
            name='rebuys_bool',
            field=models.BooleanField(default=False),
        ),
    ]
