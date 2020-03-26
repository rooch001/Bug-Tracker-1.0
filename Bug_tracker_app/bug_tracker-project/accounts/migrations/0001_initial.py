# Generated by Django 3.0.4 on 2020-03-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userName', models.CharField(max_length=30, unique=True)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('age', models.IntegerField(verbose_name='age')),
                ('mobile', models.CharField(max_length=13)),
                ('jobTitle', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('dateJoined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('lastLogin', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]