# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0006_auto_20150526_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secondary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('link', models.TextField(default=b'')),
                ('description', models.TextField(default=b'')),
                ('company', models.ForeignKey(to='query.Company')),
            ],
        ),
    ]
