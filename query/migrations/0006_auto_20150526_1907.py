# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0005_auto_20150526_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='credibility',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evidence',
            name='relevance',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
