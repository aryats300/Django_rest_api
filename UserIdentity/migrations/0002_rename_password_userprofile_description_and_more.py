# Generated by Django 4.0.5 on 2023-05-22 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserIdentity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='password',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='email',
            new_name='role_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='user_id',
        ),
    ]
