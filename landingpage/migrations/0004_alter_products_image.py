# Generated by Django 4.0.6 on 2022-07-31 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_products_discount_products_image_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]