# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-30 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('flag', models.IntegerField()),
            ],
        ),
    ]