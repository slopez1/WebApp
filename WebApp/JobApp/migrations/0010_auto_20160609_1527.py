# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-09 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0009_auto_20160609_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='grades',
            field=models.ManyToManyField(related_name='clientss', to='JobApp.Grade'),
        ),
    ]
