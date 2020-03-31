# Generated by Django 3.0.4 on 2020-03-31 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20200328_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
