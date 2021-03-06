# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2021-04-10 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('OP', 'OPEN'), ('CL', 'CLOSED')], max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
    ]
