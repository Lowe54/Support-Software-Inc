# Generated by Django 3.0 on 2020-01-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20200109_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[('AGN', 'Agent'), ('USR', 'End User')], default='USR', max_length=3),
        ),
    ]