# Generated by Django 4.2.3 on 2023-08-01 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teams",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=223)),
                ("last_name", models.CharField(max_length=223)),
                ("designation", models.CharField(max_length=223)),
                ("photo", models.ImageField(upload_to="photos/%Y/%m/%d/")),
                ("facebook_link", models.URLField(max_length=223)),
                ("twitter_link", models.URLField(max_length=223)),
                ("google_plus_link", models.URLField(max_length=223)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
