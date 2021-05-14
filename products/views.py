from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product, ProductDetails
from user.models import SearchHistory
from cart.models import Customer, Order, OrderItem
from .filters import OrderFilter

# Create your views here.

def index(request):
    search = ""
    superclassVal = ""
    subclassVal = ""
    subclasses = ""
    orderBy = "name"
    ascDesc = ""


    # default ordering
    if 'orderBy' in request.GET:
        orderBy = request.GET['orderBy']
    if 'ascDesc' in request.GET:
        ascDesc = request.GET['ascDesc']

    orderSort = ascDesc + orderBy


    # filter dropdown
    dropdown = filters(request)

    # add to cart request from products.js
    if request.method == 'POST':
        productId = request.POST['id']
        product = Product.objects.get(id=productId)
        # Get user account information
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity += 1
        orderItem.save()

        return redirect('productsIndex')


    # TODO: CODE MESS

    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        search = searchFilter

        if 'class' in request.GET:
            superclass = request.GET['class']
            superclassVal = superclass
            if 'subclass' in request.GET:
                subclass = request.GET['subclass']
                subclassVal = subclass
                products = Product.objects.filter(name__icontains=searchFilter, superclass=superclass, subclass=subclass).order_by(orderSort)
            else:
                products = Product.objects.filter(name__icontains=searchFilter, superclass=superclass).order_by(orderSort)
        else:
            products = Product.objects.filter(name__icontains=searchFilter).order_by(orderSort)


    elif 'class' in request.GET:
        superclassVal = request.GET['class']
        if 'subclass' in request.GET:
            subclass = request.GET['subclass']
            subclassVal = subclass
            products = Product.objects.filter(superclass=superclassVal, subclass=subclass).order_by(orderSort)
        else:
            products = Product.objects.filter(superclass=superclassVal).order_by(orderSort)
    else:
        products = Product.objects.all().order_by('name').order_by(orderSort)

    if superclassVal != "":
        subclasses = Product.objects.filter(superclass=superclassVal).distinct('subclass')

    return render(request, 'products/index.html', {
        'products': products,               # objects of all/filtered products
        'superclass': dropdown,             # objects of superclasses
        'search': search,                   # string value of active search
        'superclassVal': superclassVal,     # string value of active filter
        'subclassVal': subclassVal,         # string value of active filter
        'subclasses': subclasses,           # objects of subclasses
        'orderBy': orderBy,
        'ascDesc': ascDesc,
    })

def getProductById(request, id):
    if request.user.is_authenticated:
        search = SearchHistory()
        search.url = 'http://localhost:8000' + request.path
        search.user = request.user
        search.save()
    return render(request, 'products/productDetails.html',{
        'product': get_object_or_404(Product, pk=id),
        'productDetails' : get_object_or_404(ProductDetails, pk=id)
    })

def getSubclasses(request, superclass):
    subclass = list(Product.objects.filter(superclass=superclass).distinct('subclass').values())
    return JsonResponse({'data': subclass})

# Helper function

def filters(request):
    superclasses = Product.objects.all().distinct('superclass')
    return superclasses



def get_item(request):
    context = {'products': Product.objects.filter().order_by('price')}
    return render(request, 'products/index.html', context)
