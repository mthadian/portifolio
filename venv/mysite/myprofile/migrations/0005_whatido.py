# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0004_auto_20170113_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatIDo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('whyMe', models.TextField()),
                ('whatDo', models.TextField()),
                ('mission', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'What I Do',
            },
        ),
    ]
