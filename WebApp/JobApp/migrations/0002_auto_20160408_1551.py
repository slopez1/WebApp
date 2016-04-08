# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competency',
            name='area',
            field=models.CharField(max_length=15, choices=[(b'C', b'Ciencies'), (b'L', b'Lletres'), (b'A', b'Art')]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='area',
            field=models.CharField(max_length=15, choices=[(b'C', b'Ciencies'), (b'L', b'Lletres'), (b'A', b'Art')]),
        ),
        migrations.AlterField(
            model_name='job',
            name='sector',
            field=models.CharField(max_length=15, choices=[(b'p', b'primari'), (b's', b'secundari'), (b't', b'terciari')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=4, choices=[(b'd', b'dona'), (b'h', b'home')]),
        ),
    ]
