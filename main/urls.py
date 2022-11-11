from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('directions/', directions, name='directions'),
    path('schedule/', schedule, name='schedule'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('members/', members, name='members'),
    path('reviews/', reviews, name='reviews'),
]