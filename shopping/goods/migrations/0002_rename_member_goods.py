# Generated by Django 4.2.6 on 2023-10-24 12:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Member",
            new_name="Goods",
        ),
    ]