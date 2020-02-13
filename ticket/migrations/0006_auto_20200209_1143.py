# Generated by Django 3.0.2 on 2020-02-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_ticket_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OPN', 'Open'), ('PEN', 'Pending'), ('ONH', 'On Hold'), ('CLS', 'Closed')], default='OPN', max_length=3),
        ),
    ]