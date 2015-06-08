# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0011_hypothesis'),
    ]

    operations = [
        migrations.AddField(
            model_name='hypothesis',
            name='name',
            field=models.CharField(default=b'', max_length=5),
        ),
    ]
