# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-12 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20170612_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('doc', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
