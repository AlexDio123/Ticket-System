# Generated by Django 3.2 on 2021-04-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210412_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
