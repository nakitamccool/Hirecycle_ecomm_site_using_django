# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='no_of_days',
            field=models.IntegerField(default=1),
        ),
    ]
