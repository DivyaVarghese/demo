# Generated by Django 2.0 on 2019-03-21 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20190321_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 21, 16, 37, 36, 331060)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 21, 16, 37, 36, 331060)),
        ),
    ]
