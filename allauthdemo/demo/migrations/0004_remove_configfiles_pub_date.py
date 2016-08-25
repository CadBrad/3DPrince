# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_configfiles_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configfiles',
            name='pub_date',
        ),
    ]
