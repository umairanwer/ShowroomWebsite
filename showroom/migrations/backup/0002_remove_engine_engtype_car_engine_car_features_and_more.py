# Generated by Django 4.2.3 on 2023-07-30 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="engine",
            name="engType",
        ),
        migrations.AddField(
            model_name="car",
            name="engine",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="engine",
                to="showroom.engine",
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="features",
            field=models.ManyToManyField(
                related_name="features", to="showroom.carfeature"
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="mileage",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="car",
            name="model",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="carmodels",
                to="showroom.carmodel",
            ),
        ),
        migrations.AddField(
            model_name="car",
            name="price",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="engine",
            name="engCapacity",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="engine",
            name="name",
            field=models.CharField(
                blank=True, default="None Selected", max_length=50, null=True
            ),
        ),
        migrations.AddField(
            model_name="staff",
            name="showroom",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="showroom",
                to="showroom.showroom",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="name",
            field=models.CharField(default="Unnamed", max_length=50),
        ),
        migrations.AlterField(
            model_name="car",
            name="year",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="carfeature",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="carmodel",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="engine",
            name="engNum",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="showroom",
            name="address",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="showroom",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="showroom",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="showroom",
            name="telephone",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
