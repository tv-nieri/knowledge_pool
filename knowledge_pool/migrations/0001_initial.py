# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-18 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
