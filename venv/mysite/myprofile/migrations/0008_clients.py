# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0007_auto_20170118_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('No_Client', models.TextField()),
                ('No_Projects', models.TextField()),
                ('No_Exp', models.TextField()),
                ('Ongoing', models.TextField()),
            ],
        ),
    ]
