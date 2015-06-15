# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0012_hypothesis_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evidence',
            old_name='name',
            new_name='evidence',
        ),
        migrations.RenameField(
            model_name='evidence',
            old_name='link',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='evidence',
            old_name='note',
            new_name='summary',
        ),
    ]
