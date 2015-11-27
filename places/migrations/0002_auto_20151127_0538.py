# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='title',
        ),
        migrations.AddField(
            model_name='place',
            name='is_flooded',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='place',
            name='md5',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='place',
            name='osm_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='properties',
            field=models.TextField(null=True, blank=True),
        ),
    ]
