# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='mugshot',
            field=models.ImageField(null=True, upload_to='/uploads', verbose_name='头像'),
        ),
    ]
