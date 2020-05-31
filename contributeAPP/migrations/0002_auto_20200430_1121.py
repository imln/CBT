# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-30 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contributeAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ExamBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('exam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contributeAPP.Exam')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SubjectTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contributeAPP.BranchSubject')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='branchsubject',
            name='ExamBranch',
            field=models.ManyToManyField(to='contributeAPP.ExamBranch'),
        ),
    ]
