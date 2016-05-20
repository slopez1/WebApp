# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-20 11:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0006_auto_20160520_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='zodiac_sign',
            field=models.TextField(default=datetime.datetime(2016, 5, 20, 11, 23, 58, 573418, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='id_city',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='job',
            name='id_city',
            field=models.TextField(default=b''),
        ),
    ]
