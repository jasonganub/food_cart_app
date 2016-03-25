# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20160325_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeker',
            name='height',
        ),
        migrations.AddField(
            model_name='seeker',
            name='email',
            field=models.EmailField(verbose_name='email address', max_length=255, default=datetime.datetime(2016, 3, 25, 8, 33, 44, 452278, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seeker',
            name='first_name',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seeker',
            name='last_name',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seeker',
            name='user_name',
            field=models.CharField(max_length=50, default=datetime.datetime(2016, 3, 25, 8, 34, 3, 871471, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
