# Generated by Django 4.2.3 on 2023-07-31 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0002_remove_engine_engtype_car_engine_car_features_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarBrand",
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
                ("name", models.CharField(max_length=50, null=True)),
                ("pic", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.AddField(
            model_name="carmodel",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="showroom.carbrand",
            ),
        ),
    ]