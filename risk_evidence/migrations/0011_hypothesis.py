# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0010_auto_20150608_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hypothesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(default=b'')),
                ('category', models.CharField(max_length=5, choices=[(b'SCI', b'Supply Chain Impact'), (b'P', b'Probability')])),
            ],
        ),
    ]
