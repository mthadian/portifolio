# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0009_auto_20170118_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='No_Client',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='clients',
            name='No_Exp',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='clients',
            name='No_Projects',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='clients',
            name='Ongoing',
            field=models.CharField(max_length=5),
        ),
    ]
