# Generated by Django 3.0.2 on 2020-01-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20200118_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='updated_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]