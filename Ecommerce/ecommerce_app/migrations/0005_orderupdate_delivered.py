# Generated by Django 4.1.6 on 2023-02-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0004_orders_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='delivered',
            field=models.BooleanField(default=True),
        ),
    ]
