# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-05-01 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributeAPP', '0005_auto_20200501_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcquestion',
            name='ques_upload',
            field=models.ImageField(upload_to='contributeAPP/questionIMG/%Y/%m/%d/'),
        ),
    ]
