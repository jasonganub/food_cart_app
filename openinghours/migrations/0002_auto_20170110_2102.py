# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('openinghours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='closingrules',
            options={'verbose_name': 'Closing Rule', 'verbose_name_plural': 'Closing Rules', 'ordering': ['start']},
        ),
        migrations.AlterModelOptions(
            name='openinghours',
            options={'verbose_name': 'Opening Hours', 'verbose_name_plural': 'Opening Hours', 'ordering': ['company', 'weekday', 'from_hour']},
        ),
        migrations.RemoveField(
            model_name='company',
            name='slug',
        ),
        migrations.AddField(
            model_name='company',
            name='address1',
            field=models.CharField(max_length=100, verbose_name='Address1', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='address2',
            field=models.CharField(max_length=100, verbose_name='Address2', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='ethnic',
            field=models.CharField(max_length=100, verbose_name='Ethnic', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Phone', validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=localflavor.us.models.USStateField(max_length=2, verbose_name='State', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=100, verbose_name='Website', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='closingrules',
            name='company',
            field=models.ForeignKey(to='openinghours.Company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='closingrules',
            name='end',
            field=models.DateTimeField(verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='closingrules',
            name='reason',
            field=models.TextField(verbose_name='Reason', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='closingrules',
            name='start',
            field=models.DateTimeField(verbose_name='Start'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(verbose_name='Logo', null=True, upload_to='logo', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='company',
            field=models.ForeignKey(to='openinghours.Company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='from_hour',
            field=models.TimeField(verbose_name='Opening'),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='to_hour',
            field=models.TimeField(verbose_name='Closing'),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='weekday',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], verbose_name='Weekday'),
        ),
    ]
