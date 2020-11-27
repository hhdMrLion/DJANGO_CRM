# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-25 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liaison', '0006_auto_20201028_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liaison',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liaison', to='users.User', verbose_name='创建人'),
        ),
    ]