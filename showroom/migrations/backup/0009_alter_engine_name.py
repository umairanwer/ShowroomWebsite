# Generated by Django 4.2.3 on 2023-08-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0008_remove_car_id_alter_car_engine"),
    ]

    operations = [
        migrations.AlterField(
            model_name="engine",
            name="name",
            field=models.CharField(default="None Selected", max_length=50, unique=True),
        ),
    ]
