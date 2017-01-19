# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0006_imagesportifolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesportifolio',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
