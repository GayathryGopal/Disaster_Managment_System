# Generated by Django 4.1 on 2022-10-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flood", "0006_regist"),
    ]

    operations = [
        migrations.AddField(
            model_name="form",
            name="Camp_ID",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]