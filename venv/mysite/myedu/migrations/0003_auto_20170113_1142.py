# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myedu', '0002_auto_20170110_0901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'Education'},
        ),
    ]
