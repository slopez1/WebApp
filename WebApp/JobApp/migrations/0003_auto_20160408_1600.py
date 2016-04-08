# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0002_auto_20160408_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='has_competency',
            name='code_c',
            field=models.ForeignKey(to='JobApp.Competency'),
        ),
    ]
