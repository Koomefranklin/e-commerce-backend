# Generated by Django 5.0.4 on 2024-05-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_order_cart_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
    ]