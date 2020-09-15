# Generated by Django 3.0.8 on 2020-07-24 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_remove_students_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to=settings.AUTH_USER_MODEL),
        ),
    ]