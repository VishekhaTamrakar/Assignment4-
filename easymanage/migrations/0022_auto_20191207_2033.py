# Generated by Django 2.0.5 on 2019-12-08 02:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0021_auto_20191207_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_end_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 8, 2, 33, 56, 627999, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_start_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 8, 2, 33, 56, 627977, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='service_consumption_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 8, 2, 33, 56, 628440, tzinfo=utc)),
        ),
    ]
