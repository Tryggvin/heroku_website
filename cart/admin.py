from django.contrib import admin

from products.models import Product
from .models import Customer, Order, OrderItem

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class ProductAdmin(admin.ModelAdmin):
    pass

