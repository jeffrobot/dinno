# Generated by Django 2.1.5 on 2020-07-28 01:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post1', '0011_auto_20200728_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 1, 42, 45, 183520, tzinfo=utc)),
        ),
    ]
