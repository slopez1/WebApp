# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-20 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0004_auto_20160520_1003'),
    ]

    operations = [
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
