# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_articles_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='html',
            field=models.TextField(default='<p>yooo</p>'),
        ),
    ]
