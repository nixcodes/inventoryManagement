# Generated by Django 5.0.2 on 2024-02-18 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapp', '0002_alter_products_productid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Products',
        ),
    ]
