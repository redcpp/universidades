# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-03 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unsearch', '0006_auto_20160702_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busqueda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=100)),
                ('root', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('count', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'Busquedas',
                'verbose_name': 'Busqueda',
            },
        ),
    ]
