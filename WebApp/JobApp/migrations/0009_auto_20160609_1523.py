# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-09 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0008_auto_20160520_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='grades',
            field=models.ManyToManyField(related_name='clients', to='JobApp.Grade'),
        ),
    ]
