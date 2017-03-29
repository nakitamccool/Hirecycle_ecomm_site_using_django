# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0014_remove_advert_no_longer_needed'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsurancePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_package', models.CharField(choices=[(1.0, b"I don't need insurance"), (1.2, b'Bronze'), (1.4, b'Silver'), (1.5, b'Gold')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='advert',
            name='daily_insurance_cover_rate',
        ),
        migrations.RemoveField(
            model_name='advert',
            name='insurance_package',
        ),
    ]