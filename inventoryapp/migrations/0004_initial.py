# Generated by Django 5.0.2 on 2024-02-18 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventoryapp', '0003_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ProductSeq', models.AutoField(default=1000, error_messages='Error at the ProductSeq column of product table', primary_key=True, serialize=False)),
                ('ProductID', models.CharField(error_messages='Error at the ProductID column of product table', max_length=50)),
                ('ProductDesc', models.CharField(default='Description: E.g. Innova Front Wheen Bearing', error_messages='Error at the ProductDesc column of product table', max_length=50)),
                ('ProductBrand', models.CharField(default='Product Brand: SKF, NBC', error_messages='Error at the ProductBrand column of product table', max_length=50)),
                ('ProductMRP', models.DecimalField(decimal_places=2, default=0, error_messages='Error at the ProductMRP column of product table', max_digits=10)),
                ('ProductPurchasePrice', models.DecimalField(decimal_places=2, default=0, error_messages='Error at the ProductPurchasePrice column of product table', max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'unique_together': {('ProductID', 'ProductBrand')},
            },
        ),
    ]
