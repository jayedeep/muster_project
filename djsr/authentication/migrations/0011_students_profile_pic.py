# Generated by Django 3.0.8 on 2020-07-24 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_remove_students_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]