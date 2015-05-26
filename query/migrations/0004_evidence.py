# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0003_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField(default='')),
                ('note', models.TextField(default='')),
                ('link', models.TextField(default='')),
                ('country', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=30)),
                ('credibility', models.FloatField(default=0)),
                ('relevance', models.FloatField(default=0)),
                ('h1', models.IntegerField()),
                ('h2', models.IntegerField()),
                ('h3', models.IntegerField()),
                ('h4', models.IntegerField()),
                ('h5', models.IntegerField()),
                ('h6', models.IntegerField()),
                ('h7', models.IntegerField()),
                ('h8', models.IntegerField()),
                ('h9', models.IntegerField()),
                ('h10', models.IntegerField()),
                ('h11', models.IntegerField()),
                ('h12', models.IntegerField()),
                ('h13', models.IntegerField()),
                ('h14', models.IntegerField()),
                ('h15', models.IntegerField()),
                ('h16', models.IntegerField()),
                ('h17', models.IntegerField()),
                ('h18', models.IntegerField()),
                ('h19', models.IntegerField()),
                ('h20', models.IntegerField()),
                ('h21', models.IntegerField()),
                ('h22', models.IntegerField()),
                ('h23', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
