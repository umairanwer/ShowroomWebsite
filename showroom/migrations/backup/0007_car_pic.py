# Generated by Django 4.2.3 on 2023-08-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0006_rename_model_car_carmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="pic",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
