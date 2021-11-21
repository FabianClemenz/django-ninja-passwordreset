# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-02 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_rest_passwordreset", "0002_pk_migration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resetpasswordtoken",
            name="ip_address",
            field=models.GenericIPAddressField(
                blank=True,
                default="",
                null=True,
                verbose_name="The IP address of this session",
            ),
        ),
        migrations.AlterField(
            model_name="resetpasswordtoken",
            name="user_agent",
            field=models.CharField(
                blank=True, default="", max_length=256, verbose_name="HTTP User Agent"
            ),
        ),
    ]
