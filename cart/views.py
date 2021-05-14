import datetime

from django.shortcuts import render, redirect
from .models import Customer, Order, Payment, OrderItem, Contact
from cart.forms.paymentForm import PaymentForm
from cart.forms.contactForm import ContactForm
from django_countries.fields import CountryField
import uuid
from datetime import datetime
# from user.forms.profile_form import ProfileForm, UserRegisterForm
# from user.models import Profile, SearchHistory

# Create your views here.
def index(request):
    order, created, customer = getOrder(request)

    context = {'order': order}
    return render(request, 'cart/index.html', context)

def cartUpdate(request, id):
    if 'quantity' in request.POST:
        newQuantity = int(request.POST['quantity'])
        if newQuantity <= 0:
            newQuantity = 1

        OrderItem.objects.filter(id=id).update(quantity=newQuantity)

    else:
        OrderItem.objects.filter(id=id).delete()

    return redirect('cartIndex')

def paymentIndex(request):
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    year = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    try:
        info = Payment.objects.get(user_id=request.user.customer.id)
    except:
        info = ''
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        if request.user.is_active:
            customer, created = Customer.objects.get_or_create(user=request.user, name=request.user.username)
        else:
            customer, created = Customer.objects.get_or_create(device=device)
    if request.method == 'POST':
        try:
            form = PaymentForm(request.POST)
            print(request.user)
            print(request.user.customer.id)
            pay = Payment.objects.get(user_id=request.user.customer.id)
            print(pay)
            print(pay.id)
            form.save(commit=False)
            myPayment = Payment(id=pay.id, user=request.user.customer, cardOwner=form.data['cardOwner'],
                                cardNumber=form.data['cardNumber'],
                                expirationDateMonth=form.data['expirationDateMonth'],
                                expirationDateYear=form.data['expirationDateYear'],
                                cvc=form.data['cvc'])
            myPayment.save(force_update=True)
            return redirect('reviewOrder')
        except:
            form = PaymentForm(request.POST)
            if form.is_valid():
                paymentform = form.save(commit=False)
                paymentform.user = customer
                paymentform.save()
                return redirect('reviewOrder')
    return render(request, 'cart/payment.html', {
        'form': PaymentForm(),
        'year': year,
        'month': month,
        'info': info
    })

def contactIndex(request):
    countryDict = {}
    for country in CountryField().countries:
        countryDict[country[0]] = country[1]
    try:
        info = Contact.objects.get(customer_id=request.user.customer.id)
    except:
        info = ''
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        if request.user.is_active:
            customer, created = Customer.objects.get_or_create(user=request.user, name=request.user.username)
        else:
            customer, created = Customer.objects.get_or_create(device=device)
    if request.method == 'POST':
        try:
            form = ContactForm(request.POST)
            print(request.user)
            print(request.user.customer.id)
            contact = Contact.objects.get(customer_id=request.user.customer.id)
            print(contact)
            print(contact.id)
            form.save(commit=False)
            myContact = Contact(id=contact.id,name=form.data['name'], streetName=form.data['streetName'],
                          houseNumber=form.data['houseNumber'], city=form.data['city'],
                          country=form.data['country'], postalCode=form.data['postalCode'],
                          customer_id=request.user.customer.id)
            myContact.save(force_update=True)
            return redirect('payment')
        except:
            form = ContactForm(request.POST)
            if form.is_valid():
                contactform = form.save(commit=False)
                contactform.customer = customer
                contactform.save()
                return redirect('payment')
    return render(request, 'cart/contact.html', {
        'form': ContactForm(),
        'info': info,
        'countryDict': countryDict
    })

def reviewOrder(request):

    order, created, customer = getOrder(request)

    contact = Contact.objects.filter(customer=customer).first()

    payment = Payment.objects.filter(user=customer).last()
    creditCard = ""
    try:
        creditstr = payment.cardNumber
        creditCard = creditstr[:4]
    except:
        creditCard = ""

    if request.method == 'POST':
        transId = str(uuid.uuid4())
        now = datetime.now()
        Order.objects.filter(customer=customer, complete=False).update(complete=True, transactionId=transId, dateOrdered=now)

        return render(request, 'cart/receipt.html', {
            'order': order,
            'transId': transId,
            'customer': request.user
        })


    return render(request, 'cart/review.html', {
        'order': order,
        'contact': contact,
        'payment': payment,
        'creditCard': creditCard
    })


# helper functions
def getOrder(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        if request.user.is_active:
            customer, created = Customer.objects.get_or_create(user=request.user, name=request.user.username)
        else:
            customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    return order, created, customer
