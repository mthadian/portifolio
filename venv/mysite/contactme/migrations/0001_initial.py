# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=30)),
                ('Message', models.CharField(max_length=5000)),
            ],
            options={
                'verbose_name_plural': 'Contact Me',
            },
        ),
    ]
