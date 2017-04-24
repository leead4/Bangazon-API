# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BangazonAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type_provider', models.CharField(max_length=25)),
                ('account_number', models.CharField(max_length=25)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_types', related_query_name='payment_types', to='BangazonAPI.Customer')),
            ],
        ),
    ]
