from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cartIndex"),
    path('<int:id>', views.cartUpdate, name='cartItem'),
    path('payment', views.paymentIndex, name='payment'),
    path('contact', views.contactIndex, name='contact'),
    path('review', views.reviewOrder, name='reviewOrder')
]