# Generated by Django 3.0.8 on 2020-07-24 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_students_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('College', 'College'), ('Professor', 'Professor'), ('Student', 'Student')], max_length=100),
        ),
    ]
