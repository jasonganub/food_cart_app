# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20160324_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeker',
            name='home_town',
        ),
    ]
