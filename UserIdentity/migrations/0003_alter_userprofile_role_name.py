# Generated by Django 4.0.5 on 2023-05-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserIdentity', '0002_rename_password_userprofile_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role_name',
            field=models.CharField(max_length=100),
        ),
    ]