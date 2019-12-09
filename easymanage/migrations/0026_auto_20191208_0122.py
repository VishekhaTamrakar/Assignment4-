# Generated by Django 2.0.5 on 2019-12-08 07:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0025_auto_20191208_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_end_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 8, 7, 22, 46, 682685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_start_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 8, 7, 22, 46, 682661, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='service_consumption_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 8, 7, 22, 46, 683143, tzinfo=utc)),
        ),
    ]
