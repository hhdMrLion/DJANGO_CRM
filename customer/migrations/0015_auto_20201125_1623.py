# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-25 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_remove_customer_belong_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='users.User', verbose_name='创建人'),
        ),
    ]
