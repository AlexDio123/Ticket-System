# Generated by Django 3.2 on 2021-04-13 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_username'),
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
