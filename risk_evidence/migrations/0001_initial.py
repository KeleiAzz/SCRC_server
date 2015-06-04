# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('letter_scale', models.CharField(max_length=10, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C'), (b'High', b'High'), (b'Medium', b'Medium'), (b'Low', b'Low')])),
                ('num_scale', models.FloatField(null=True, blank=True)),
                ('category', models.CharField(max_length=5, choices=[(b'SCI', b'Supply Chain Impact'), (b'P', b'Probability')])),
                ('definition', models.TextField(default=b'')),
                ('sub_category', models.CharField(max_length=15, choices=[(b'Credibility', b'Credibility'), (b'Revelance', b'Revelance')])),
            ],
        ),
    ]
