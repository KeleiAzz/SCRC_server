# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0002_auto_20150604_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='sub_category',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[(b'Credibility', b'Credibility'), (b'Revelance', b'Revelance')]),
        ),
    ]
