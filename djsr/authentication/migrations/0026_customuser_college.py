# Generated by Django 3.0.8 on 2020-08-03 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0025_remove_customuser_abc'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='college',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
