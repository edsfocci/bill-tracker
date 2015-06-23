# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotation_app', '0002_auto_20150618_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='ranges_end',
            field=models.CharField(null=True, max_length=255),
        ),
        migrations.AddField(
            model_name='annotation',
            name='ranges_start',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
