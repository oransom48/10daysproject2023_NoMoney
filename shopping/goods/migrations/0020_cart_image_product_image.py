# Generated by Django 4.2.6 on 2023-10-29 06:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0019_alter_goods_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image'),
            preserve_default=False,
        ),
    ]