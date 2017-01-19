# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_delete_mydescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='Mobile',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='intro',
            name='Mobile1',
            field=models.CharField(max_length=15),
        ),
    ]
