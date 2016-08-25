# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_remove_configfiles_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='configfiles',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined', blank=True),
        ),
    ]
