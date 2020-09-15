# Generated by Django 3.0.8 on 2020-08-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0028_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='today_attendance',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='username',
        ),
        migrations.AddField(
            model_name='attendance',
            name='sem',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]