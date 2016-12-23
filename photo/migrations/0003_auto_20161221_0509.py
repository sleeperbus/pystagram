# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20161221_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='filtered_image_file',
            field=models.ImageField(upload_to=b'static_files/uploaded/filtered/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to=b'static_files/uploaded/original/%Y/%m/%d'),
        ),
    ]
