from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    archived = models.BooleanField()
    image = models.CharField(max_length=9999, blank=True)
    description = models.CharField(max_length=255, blank=True)
    superclass = models.CharField(max_length=255)
    subclass = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=9999)
    image1 = models.CharField(max_length=9999)
    image2 = models.CharField(max_length=9999, blank=True, null=True, default="")
    def __str__(self):
        return self.product.name
