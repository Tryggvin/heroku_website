from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    #path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('login', views.loginIn, name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('history', views.history, name='history'),
    path('payment', views.payment, name='payment12'),
    path('names', views.names, name='names')
]