# Generated by Django 4.2.6 on 2023-10-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0018_alter_goods_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goods",
            name="image",
            field=models.ImageField(upload_to="image"),
        ),
    ]