# Generated by Django 2.0.5 on 2019-12-09 19:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0029_auto_20191208_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerservice',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_end_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 9, 19, 48, 20, 823922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_start_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 9, 19, 48, 20, 823898, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='service_consumption_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 9, 19, 48, 20, 824408, tzinfo=utc)),
        ),
    ]
