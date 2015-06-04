# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='sub_category',
            field=models.CharField(max_length=15, null=True, choices=[(b'Credibility', b'Credibility'), (b'Revelance', b'Revelance')]),
        ),
    ]
