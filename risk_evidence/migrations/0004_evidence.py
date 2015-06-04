# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0003_auto_20150604_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'')),
                ('note', models.TextField(default=b'')),
                ('link', models.TextField(default=b'')),
                ('country', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=5, choices=[(b'SCI', b'Supply Chain Impact'), (b'P', b'Probability')])),
                ('credibility', models.CharField(max_length=10, choices=[(b'High', b'High'), (b'Medium', b'Medium'), (b'Low', b'Low')])),
                ('revelance', models.CharField(max_length=10, choices=[(b'High', b'High'), (b'Medium', b'Medium'), (b'Low', b'Low')])),
                ('h1', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h2', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h3', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h4', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h5', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h6', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h7', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h8', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h9', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h10', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h11', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h12', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h13', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h14', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h15', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h16', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h17', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h18', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h19', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h20', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h21', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h22', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
                ('h23', models.CharField(max_length=5, choices=[(b'I I', b'I I'), (b'I', b'I'), (b'NA', b'NA'), (b'N', b'N'), (b'C', b'C'), (b'C C', b'C C')])),
            ],
        ),
    ]
