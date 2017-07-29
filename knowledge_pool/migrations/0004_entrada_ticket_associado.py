# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-29 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_pool', '0003_remove_assunto_ticket_associado'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='ticket_associado',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
