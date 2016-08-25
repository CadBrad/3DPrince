# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import allauthdemo.demo.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HDConfig', models.FileField(upload_to=allauthdemo.demo.models.UploadedConfigPath, verbose_name='High Detail')),
                ('LDConfig', models.FileField(upload_to=allauthdemo.demo.models.UploadedConfigPath, verbose_name='Low Detail')),
                ('Printer', models.CharField(max_length=100, null=True, verbose_name='Printer Model', blank=True)),
                ('Plastic', models.CharField(max_length=40, null=True, verbose_name='Plastic', blank=True)),
                ('creator', models.CharField(max_length=40, null=True, verbose_name='Creator', blank=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('STL', models.FileField(upload_to=allauthdemo.demo.models.user_directory_path, verbose_name='STL Upload')),
                ('Photo', models.ImageField(upload_to=allauthdemo.demo.models.user_directory_path, verbose_name='Photo')),
                ('Title', models.CharField(max_length=40, null=True, verbose_name='Title of object', blank=True)),
                ('Category', models.CharField(max_length=40, null=True, verbose_name='Category', blank=True)),
                ('SubCategory', models.CharField(max_length=40, null=True, verbose_name='SubCategory', blank=True)),
                ('SubSubCategory', models.CharField(max_length=40, null=True, verbose_name='SubSubCategory_field', blank=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined')),
            ],
        ),
    ]
