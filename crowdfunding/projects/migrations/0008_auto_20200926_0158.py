# Generated by Django 3.0.8 on 2020-09-26 01:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_no_pledges'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 26, 1, 58, 20, 519923, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='project_update',
            name='project_update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 26, 1, 58, 20, 554437, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 26, 1, 58, 20, 519890, tzinfo=utc)),
        ),
    ]
