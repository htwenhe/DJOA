# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-23 09:31
from __future__ import unicode_literals
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='createdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间'),
        ),
    ]
