# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0006_auto_20170329_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='insurance_package',
            field=models.DecimalField(choices=[(1.0, b'No_insurance'), (1.2, b'Bronze'), (1.4, b'Silver'), (1.5, b'Gold')], decimal_places=2, default=None, max_digits=6),
        ),
    ]
