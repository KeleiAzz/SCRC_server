# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_evidence', '0007_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(default=None, unique=True, max_length=50, choices=[(b'ARGENTINA', b'ARGENTINA'), (b'AUSTRALIA', b'AUSTRALIA'), (b'BANGLADESH', b'BANGLADESH'), (b'BOSNIA', b'BOSNIA'), (b'BRAZIL', b'BRAZIL'), (b'BULGARIA', b'BULGARIA'), (b'CAMBODIA', b'CAMBODIA'), (b'CANADA', b'CANADA'), (b'CHINA', b'CHINA'), (b'ECUADOR', b'ECUADOR'), (b'EGYPT', b'EGYPT'), (b'EL SALVADOR', b'EL SALVADOR'), (b'GEORGIA', b'GEORGIA'), (b'GUATEMALA', b'GUATEMALA'), (b'HONDURAS', b'HONDURAS'), (b'HONG KONG (CHINA)', b'HONG KONG (CHINA)'), (b'INDIA', b'INDIA'), (b'INDONESIA', b'INDONESIA'), (b'ISRAEL', b'ISRAEL'), (b'ITALY', b'ITALY'), (b'JAPAN', b'JAPAN'), (b'JORDAN', b'JORDAN'), (b'MACAU (CHINA)', b'MACAU (CHINA)'), (b'MALAYSIA', b'MALAYSIA'), (b'MEXICO', b'MEXICO'), (b'MOLDOVA', b'MOLDOVA'), (b'NETHERLANDS', b'NETHERLANDS'), (b'NICARAGUA', b'NICARAGUA'), (b'PAKISTAN', b'PAKISTAN'), (b'PARAGUAY', b'PARAGUAY'), (b'PERU', b'PERU'), (b'PHILIPPINES', b'PHILIPPINES'), (b'POLAND', b'POLAND'), (b'PORTUGAL', b'PORTUGAL'), (b'SOUTH AFRICA', b'SOUTH AFRICA'), (b'SOUTH KOREA', b'SOUTH KOREA'), (b'SPAIN', b'SPAIN'), (b'SRI LANKA', b'SRI LANKA'), (b'TAIWAN', b'TAIWAN'), (b'THAILAND', b'THAILAND'), (b'TURKEY', b'TURKEY'), (b'UNITED KINGDOM', b'UNITED KINGDOM'), (b'USA', b'USA'), (b'VIETNAM', b'VIETNAM')]),
        ),
    ]
