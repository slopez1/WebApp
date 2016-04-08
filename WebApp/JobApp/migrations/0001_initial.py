# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='competency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_c', models.IntegerField()),
                ('name_c', models.TextField(max_length=50)),
                ('area', models.CharField(unique=True, max_length=15, choices=[(b'C', b'Ciencies'), (b'L', b'Lletres'), (b'A', b'Art')])),
                ('description', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_g', models.IntegerField()),
                ('name_g', models.TextField(max_length=50)),
                ('area', models.CharField(unique=True, max_length=15, choices=[(b'C', b'Ciencies'), (b'L', b'Lletres'), (b'A', b'Art')])),
                ('description', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Has_Competency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experience_since_year', models.IntegerField()),
                ('code_c', models.ForeignKey(to='JobApp.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Has_Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year_start', models.IntegerField()),
                ('year_finished', models.IntegerField()),
                ('code_g', models.ForeignKey(to='JobApp.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_j', models.IntegerField()),
                ('name', models.TextField(max_length=50)),
                ('sector', models.CharField(unique=True, max_length=15, choices=[(b'p', b'primari'), (b's', b'secundari'), (b't', b'terciari')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_u', models.IntegerField()),
                ('name', models.TextField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(unique=True, max_length=4, choices=[(b'd', b'dona'), (b'h', b'home')])),
                ('is_looking_for_job', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='has_grade',
            name='code_u',
            field=models.ForeignKey(to='JobApp.User'),
        ),
        migrations.AddField(
            model_name='has_competency',
            name='code_u',
            field=models.ForeignKey(to='JobApp.User'),
        ),
    ]
