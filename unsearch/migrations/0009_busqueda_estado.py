# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-03 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unsearch', '0008_remove_busqueda_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='busqueda',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='busquedas', to='unsearch.Estado'),
            preserve_default=False,
        ),
    ]
