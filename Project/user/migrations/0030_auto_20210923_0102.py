# Generated by Django 3.2.6 on 2021-09-22 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_auto_20210921_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazondata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 1, 2, 50, 831626)),
        ),
        migrations.AlterField(
            model_name='flipkartdata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 1, 2, 50, 831626)),
        ),
        migrations.AlterField(
            model_name='snapdealdata',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 1, 2, 50, 831626)),
        ),
    ]
