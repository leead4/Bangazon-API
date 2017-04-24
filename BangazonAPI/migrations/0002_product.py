# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BangazonAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=25)),
                ('product_price', models.IntegerField()),
                ('product_description', models.CharField(max_length=25)),
                ('customer_id', models.CharField(max_length=25)),
                ('product_type_id', models.CharField(max_length=25)),
            ],
        ),
    ]
