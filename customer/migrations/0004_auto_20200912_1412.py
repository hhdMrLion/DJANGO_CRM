# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-12 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200911_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinvoiceaddress',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='是否有效'),
        ),
        migrations.AddField(
            model_name='customershopaddress',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='是否有效'),
        ),
    ]
