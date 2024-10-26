from django.db import models



class Products(models.Model):
    ProductSeq = models.AutoField(primary_key=True, error_messages="Error at the ProductSeq column of product table")
    ProductID = models.CharField(max_length=50, null=False, error_messages="Error at the ProductID column of product table")
    ProductDesc = models.CharField(max_length=50, default="Description: E.g. Innova Front Wheen Bearing", error_messages="Error at the ProductDesc column of product table")
    ProductBrand = models.CharField(max_length=50, null=False, default="Product Brand: SKF, NBC", error_messages="Error at the ProductBrand column of product table")
    ProductMRP = models.DecimalField(max_digits=10, null=False, decimal_places=2, default=0, error_messages="Error at the ProductMRP column of product table")
    ProductPurchasePrice = models.DecimalField(max_digits=10, null=False, decimal_places=2, default=0, error_messages="Error at the ProductPurchasePrice column of product table")

    class Meta:
        unique_together = ('ProductID', 'ProductBrand')
        verbose_name_plural = "Products"