# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0005_whatido'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesPortifolio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('project', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Portifolio',
            },
        ),
    ]
