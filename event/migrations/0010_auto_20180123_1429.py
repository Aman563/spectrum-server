# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-23 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20180122_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdata',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='eventdata',
            name='rules',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
