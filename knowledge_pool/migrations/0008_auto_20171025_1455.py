# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_pool', '0007_assunto_qnt_entradas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assunto',
            name='qnt_entradas',
            field=models.IntegerField(default=0),
        ),
    ]
