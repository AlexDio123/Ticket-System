# Generated by Django 3.2 on 2021-04-13 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20210412_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
    ]
