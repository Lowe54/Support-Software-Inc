# Generated by Django 3.0 on 2020-01-18 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20200118_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='Raised On',
            new_name='raised_on',
        ),
    ]