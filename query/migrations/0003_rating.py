# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('score', models.FloatField(default=0)),
                ('expire_date', models.DateField(default=None)),
                ('category', models.ForeignKey(to='query.Category')),
                ('company', models.ForeignKey(to='query.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
