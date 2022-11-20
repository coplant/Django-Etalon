from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('directions/', DirectionsView.as_view(), name='directions'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('reviews/', ReviewView.as_view(), name='reviews'),
    path('subscriptions/', SubscriptionView.as_view(), name='subscriptions'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('members/', CoachView.as_view(), name='members'),


    # path('user/', user, name='user'),
    path('logout/', logout_user, name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='main/templates/registration/login.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name=''), name='login'),
]