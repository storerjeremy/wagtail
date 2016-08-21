# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='path',
            field=models.CharField(max_length=191, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='path',
            field=models.CharField(max_length=191, unique=True),
        ),
    ]