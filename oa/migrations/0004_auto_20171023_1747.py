# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-23 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0003_auto_20171023_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='title_a',
        ),
    ]
