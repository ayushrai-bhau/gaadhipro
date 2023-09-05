# Generated by Django 4.2.3 on 2023-08-28 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="create_date",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="user_id",
            field=models.IntegerField(blank=True),
        ),
    ]
