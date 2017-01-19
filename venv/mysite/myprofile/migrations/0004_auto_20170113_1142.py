# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0003_auto_20170111_0213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intro',
            options={'verbose_name_plural': 'Introduction'},
        ),
    ]
