from .models import Order, Customer
import uuid

def orderItemRender(request):
    try:
        device = request.COOKIES['device']
    except:
        device = str(uuid.uuid4())
    try:
        customer = request.user.customer
    except:
        if request.user.is_active:
            customer, created = Customer.objects.get_or_create(user=request.user, name=request.user.username)
        else:
            customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    return {
        'allItems': order,
    }