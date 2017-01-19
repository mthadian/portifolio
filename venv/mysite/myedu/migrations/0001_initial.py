# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myEducation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Duration', models.CharField(max_length=20)),
                ('Degree', models.CharField(max_length=50)),
                ('Institution', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=2000)),
            ],
        ),
    ]
