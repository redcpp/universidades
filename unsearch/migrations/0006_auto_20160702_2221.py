# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unsearch', '0005_estado_municipios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='municipios',
            field=models.IntegerField(default=0),
        ),
    ]