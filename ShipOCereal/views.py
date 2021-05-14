from django.shortcuts import render
from django.db.models import Count
from products.models import Product
from cart.models import OrderItem

# Create your views here.
def index(request):

    # gets 4 most popular items according to how many people have them in a cart
    context =  OrderItem.objects.values('product_id', 'product__price', 'product__name', 'product__image').annotate(c=Count('product_id')).order_by('-c')[:4]
    return render(request, 'home/index.html', {
        'products': context,
        'test1': "test"
    })
