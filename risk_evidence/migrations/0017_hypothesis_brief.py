# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0016_factory'),
    ]

    operations = [
        migrations.AddField(
            model_name='hypothesis',
            name='brief',
            field=models.TextField(default=b''),
        ),
    ]
