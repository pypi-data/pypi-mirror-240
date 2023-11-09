# Generated by Django 3.2.8 on 2021-10-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("offer", "0011_conditionaloffer_affects_cosmetic_pricing"),
    ]

    operations = [
        migrations.CreateModel(
            name="BluelightFixedPricePerItemBenefit",
            fields=[],
            options={
                "verbose_name": "Fixed price per item benefit",
                "verbose_name_plural": "Fixed price per item benefits",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("offer.fixedpricebenefit",),
        ),
        migrations.AddField(
            model_name="benefit",
            name="max_discount",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="If set, do not allow this benefit to provide a discount greater than this amount (for a particular basket application).",
                max_digits=12,
                null=True,
                verbose_name="Max discount",
            ),
        ),
    ]
