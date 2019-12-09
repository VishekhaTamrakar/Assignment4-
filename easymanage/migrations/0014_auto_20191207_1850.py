# Generated by Django 2.0.5 on 2019-12-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0013_auto_20191105_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_end_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
