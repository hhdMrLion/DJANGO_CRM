# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-24 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_auto_20200924_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='invoice_city',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='发票市区'),
        ),
    ]