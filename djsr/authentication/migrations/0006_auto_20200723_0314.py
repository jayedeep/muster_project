# Generated by Django 3.0.8 on 2020-07-23 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20200721_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='college',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]