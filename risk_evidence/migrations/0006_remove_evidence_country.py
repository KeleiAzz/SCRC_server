# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0005_auto_20150608_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidence',
            name='country',
        ),
    ]
