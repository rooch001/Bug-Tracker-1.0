# Generated by Django 3.0.4 on 2020-03-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200328_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_file',
            field=models.FileField(default=None, upload_to='files/project_file/'),
            preserve_default=False,
        ),
    ]
