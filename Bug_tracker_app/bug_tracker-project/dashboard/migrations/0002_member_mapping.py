# Generated by Django 3.0.4 on 2020-03-28 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200328_1205'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Project')),
            ],
        ),
    ]
