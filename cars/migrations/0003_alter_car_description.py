# Generated by Django 4.2.3 on 2023-08-05 00:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_alter_car_is_featured_alter_car_passenger"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="description",
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
    ]