# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=20)),
                ('bloomberg_ticker', models.CharField(max_length=20)),
                ('website', models.TextField(default='')),
                ('industry_group', models.CharField(max_length=100)),
                ('industry_subgroup', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
