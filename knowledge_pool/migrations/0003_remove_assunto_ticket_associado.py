# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-29 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_pool', '0002_assunto_ticket_associado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assunto',
            name='ticket_associado',
        ),
    ]
