# Generated by Django 4.2.6 on 2023-10-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0014_product_remove_ordered_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordered",
            name="paid",
            field=models.BooleanField(default=False),
        ),
    ]