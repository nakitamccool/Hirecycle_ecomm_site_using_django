# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0012_auto_20170329_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='no_longer_needed',
            field=models.CharField(default=1.0, max_length=100),
        ),
        migrations.AlterField(
            model_name='advert',
            name='insurance_package',
            field=models.DecimalField(choices=[(1.0, b"I don't need insurance"), (1.2, b'Bronze'), (1.4, b'Silver'), (1.5, b'Gold')], decimal_places=2, max_digits=10),
        ),
    ]