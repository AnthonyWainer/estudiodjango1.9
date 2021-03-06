# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clase1', '0003_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
