# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Period', models.CharField(max_length=15)),
                ('Institution', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=2000)),
            ],
        ),
    ]
