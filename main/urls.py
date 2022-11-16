from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', MainView.as_view(), name='home'),
    path('directions/', DirectionsView.as_view(), name='directions'),
    path('schedule/', schedule, name='schedule'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('members/', members, name='members'),
    path('reviews/', reviews, name='reviews'),


    # path('user/', user, name='user'),
    path('user/', include('django.contrib.auth.urls'), name='login')
    # path('login/', auth_views.LoginView.as_view(template_name='main/templates/registration/login.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name=''), name='login'),
]