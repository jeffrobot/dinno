# Generated by Django 2.1.5 on 2020-07-27 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post1', '0006_auto_20200727_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 7, 35, 30, 577254, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='gender',
            field=models.BooleanField(default=False),
        ),
    ]
