# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0006_auto_20161114_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='related_compounds',
        ),
        migrations.AddField(
            model_name='compound',
            name='related_compound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_compounds', to='compounds.Compound'),
        ),
    ]