# Generated by Django 5.0.6 on 2024-06-17 19:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_suburbio', '0002_user_alter_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
