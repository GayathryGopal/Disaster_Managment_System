# Generated by Django 4.1 on 2022-10-01 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flood", "0003_rename_flood_floods"),
    ]

    operations = [
        migrations.AlterField(
            model_name="floods",
            name="Camp_Name",
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name="floods", name="Camp_id", field=models.IntegerField(),
        ),
    ]