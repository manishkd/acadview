# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_text', models.CharField(max_length=200)),
                ('roll_no', models.CharField(max_length=200)),
                ('present', models.IntegerField(default=0)),
                ('absent', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_text', models.CharField(max_length=200)),
                ('subject_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='subsem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='att.Subject'),
        ),
    ]
