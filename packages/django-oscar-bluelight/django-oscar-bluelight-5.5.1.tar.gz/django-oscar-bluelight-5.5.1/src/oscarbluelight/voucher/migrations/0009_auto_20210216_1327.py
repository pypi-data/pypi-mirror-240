# Generated by Django 3.1.6 on 2021-02-16 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("voucher", "0008_auto_20200801_0817"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="voucher",
            options={
                "base_manager_name": "objects",
                "ordering": (
                    "-offers__offer_group__priority",
                    "-offers__priority",
                    "pk",
                ),
            },
        ),
    ]
