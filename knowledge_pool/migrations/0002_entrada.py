# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-18 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_pool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('assunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge_pool.Assunto')),
            ],
        ),
    ]
