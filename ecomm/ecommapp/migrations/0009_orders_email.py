# Generated by Django 5.0.1 on 2024-02-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0008_rename_carts_orders_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]