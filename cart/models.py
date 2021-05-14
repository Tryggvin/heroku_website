from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django_countries.fields import CountryField

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    device = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    dateOrdered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True)
    transactionId = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id) + " | " #+ str(self.customer.name)

    @property
    def getCartTotal(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def getCartItems(self):
        orderitems = self.orderitem_set.all()
        return orderitems

    @property
    def getNumItems(self):
        orderitems = self.orderitem_set.all()
        totalitems = sum([item.quantity for item in orderitems])
        return totalitems


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "order: " + str(self.order) + "| product: " + str(self.product.name)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total




class Payment(models.Model):
    class Month(models.IntegerChoices):
        JAN = 1, "01"
        FEB = 2, "02"
        MAR = 3, "03"
        APR = 4, "04"
        MAY = 5, "05"
        JUN = 6, "06"
        JUL = 7, "07"
        AUG = 8, "08"
        SEP = 9, "09"
        OCT = 10, "10"
        NOV = 11, "11"
        DES = 12, "12"

    class Year(models.IntegerChoices):
        TW1 = 21, "21"
        TW2 = 22, "22"
        TW3 = 23, "23"
        TW4 = 24, "24"
        TW5 = 25, "25"
        TW6 = 26, "26"
        TW7 = 27, "27"
        TW8 = 28, "28"
        TW9 = 29, "29"
        TH0 = 30, "30"



    user = models.OneToOneField(Customer, on_delete=models.CASCADE, unique=True)
    cardOwner = models.CharField(max_length=100, null=True)
    cardNumber = models.CharField(max_length=19, null=True)
    expirationDateMonth = models.PositiveSmallIntegerField(choices=Month.choices,
        default=Month.JAN)
    expirationDateYear = models.PositiveSmallIntegerField(choices=Year.choices,
        default=Year.TW2)
    cvc = models.CharField(max_length=3, null=True)


class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    streetName = models.CharField(max_length=100, null=True)
    houseNumber = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=100, null=True)
    country = CountryField()
    postalCode = models.PositiveBigIntegerField()