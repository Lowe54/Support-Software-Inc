# Generated by Django 3.0.2 on 2020-02-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_order_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
