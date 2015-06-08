# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0004_evidence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evidence',
            old_name='revelance',
            new_name='relevance',
        ),
        migrations.AlterField(
            model_name='score',
            name='sub_category',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[(b'Credibility', b'Credibility'), (b'Relevance', b'Relevance')]),
        ),
    ]
