# Generated by Django 3.2 on 2021-04-13 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20210413_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
