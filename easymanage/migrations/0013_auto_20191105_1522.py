# Generated by Django 2.0.5 on 2019-11-05 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0012_remove_roomstatus_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerservice',
            name='location',
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='service_category',
            field=models.CharField(choices=[('Food', 'Food'), ('Beverages', 'Beverages'), ('Food&Beverages', 'Food&Beverages'), ('MaintenanceCost', 'MaintenanceCost')], default='Food', max_length=10),
        ),
    ]
