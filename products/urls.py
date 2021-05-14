from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="productsIndex"),
    path('<int:id>', views.getProductById, name='products'),
    path('class/<str:superclass>', views.getSubclasses, name="subclasses")
]