# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-14 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='doc',
            field=models.FileField(default='', upload_to='', verbose_name='Pdf of resume'),
        ),
    ]
