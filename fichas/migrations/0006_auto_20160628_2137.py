# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 21:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0005_auto_20160628_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abono',
            old_name='paciente',
            new_name='cliente',
        ),
    ]