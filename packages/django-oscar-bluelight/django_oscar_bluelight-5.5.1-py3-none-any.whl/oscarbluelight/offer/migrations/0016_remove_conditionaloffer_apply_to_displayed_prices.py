# Generated by Django 2.1.7 on 2019-06-06 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0015_auto_20181018_1220"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="conditionaloffer",
            name="apply_to_displayed_prices",
        ),
    ]
