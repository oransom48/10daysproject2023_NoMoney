# Generated by Django 4.2.6 on 2023-10-27 00:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0009_alter_cart_price_alter_cart_quantity_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
        migrations.AddField(
            model_name="cart",
            name="product_id",
            field=models.IntegerField(null=True),
        ),
    ]
