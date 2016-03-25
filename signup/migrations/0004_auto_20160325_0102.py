# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_remove_seeker_home_town'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeker',
            name='user',
        ),
        migrations.AddField(
            model_name='seeker',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='seeker',
            name='password',
            field=models.CharField(default=datetime.datetime(2016, 3, 25, 8, 2, 10, 724070, tzinfo=utc), max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
