# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0008_clients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterField(
            model_name='clients',
            name='No_Client',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clients',
            name='No_Exp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clients',
            name='No_Projects',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clients',
            name='Ongoing',
            field=models.IntegerField(),
        ),
    ]
