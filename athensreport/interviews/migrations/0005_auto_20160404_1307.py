# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-04 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0004_auto_20160402_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sex',
            field=models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female')], default=b'Male', max_length=10),
        ),
    ]