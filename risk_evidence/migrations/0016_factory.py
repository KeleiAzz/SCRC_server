# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0015_auto_20150614_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'')),
                ('product_type', models.CharField(default=b'', max_length=20)),
                ('brand', models.CharField(default=b'', max_length=25)),
                ('event', models.TextField(default=b'')),
                ('address', models.TextField(default=b'')),
                ('city', models.CharField(default=b'', max_length=50)),
                ('state', models.CharField(default=b'', max_length=50)),
                ('postal_code', models.CharField(default=b'', max_length=30)),
                ('country', models.CharField(default=b'', max_length=30)),
                ('operating_region', models.CharField(default=b'', max_length=30)),
                ('total_workers', models.IntegerField(default=0)),
                ('line_workers', models.IntegerField(default=0)),
                ('female_percent', models.FloatField(default=0.0)),
                ('migrant_percent', models.FloatField(default=0.0)),
            ],
        ),
    ]
