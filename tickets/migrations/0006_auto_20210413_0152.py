# Generated by Django 3.2 on 2021-04-13 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20210410_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='end_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='start_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
