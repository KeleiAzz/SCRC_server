# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0014_auto_20150612_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hypothesis',
            name='name',
        ),
        migrations.AlterModelOptions(
            name='hypothesis',
            options={'ordering': ('num',)},
        ),
        migrations.AddField(
            model_name='hypothesis',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='hypothesis',
            unique_together=set([('num', 'category')]),
        ),

    ]
