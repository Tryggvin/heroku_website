from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user.forms.profile_form import ProfileForm, UserRegisterForm
from user.models import Profile, SearchHistory
from cart.forms.paymentForm import PaymentForm
from cart.models import Customer, Payment
from products.models import Product
from django.http import JsonResponse
# Create your views here.


def register(request):
    if request.method != 'POST':
        return render(request, 'user/register.html', {
            'form': UserRegisterForm()
        })
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            user = Profile()
            user.user = User.objects.get(id=task.id)
            user.profileImage = 'https://d1nhio0ox7pgb.cloudfront.net/_img/o_collection_png/green_dark_grey/512x512/plain/user.png'
            user.firstName = form.cleaned_data['first_name']
            user.lastName = form.cleaned_data['last_name']
            user.save()
            return redirect('login')
    return render(request, 'user/register.html',{
        'form': UserRegisterForm()
    })


def profile(request):
    # Edit profile
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            user = Profile.objects.get(user=request.user.id)
            user = user.user
            user.first_name = request.POST['firstName']
            user.last_name = request.POST['lastName']
            user.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile),
        'profile': profile
    })


def history(request):
    idList = []
    newDict = {}
    for x in SearchHistory.objects.filter(user_id=request.user.id).order_by('-time')[:10]:
        y = x.time
        x = x.url
        x = x.split('/')
        x = x[-1]
        idList.append(int(x))
        newDict[Product.objects.filter(id=x)] = y
        # newList.append(y)
    print(newDict)
    context = {'SearchHistory': SearchHistory.objects.filter(user_id=request.user.id).order_by('-time')[:10],
               'products': newDict
               }
    return render(request, 'user/history.html', context)

def loginIn(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homeIndex')
        else:
            return render(request, 'user/login.html')



def payment(request):
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
            return redirect('payment12')
        except:
            form = PaymentForm(request.POST)
            if form.is_valid():
                paymentform = form.save(commit=False)
                paymentform.user = customer
                paymentform.save()
                return render(request, 'cart/index.html')
    return render(request, 'user/payment12.html', {
        'form': PaymentForm(),
        'year': year,
        'month': month,
        'info': info
    })

def names(request):
    username = list(User.objects.all().values('username'))
    return JsonResponse({'data': username})