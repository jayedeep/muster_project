# Generated by Django 3.0.8 on 2020-08-02 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_auto_20200802_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='created_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
