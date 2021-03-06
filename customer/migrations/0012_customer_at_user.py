# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-25 02:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0011_customer_invoice_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='at_user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='at_customer', to=settings.AUTH_USER_MODEL, verbose_name='负责人'),
            preserve_default=False,
        ),
    ]
