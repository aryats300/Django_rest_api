# Generated by Django 4.0.5 on 2023-05-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileStorage', '0004_remove_upload_file_id_upload_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='id',
        ),
        migrations.AddField(
            model_name='upload',
            name='file_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
