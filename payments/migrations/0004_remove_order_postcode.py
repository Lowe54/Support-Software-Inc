# Generated by Django 3.0.2 on 2020-02-09 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20200209_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='postcode',
        ),
    ]
