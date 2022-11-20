from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('directions/', DirectionsView.as_view(), name='directions'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('reviews/', AddReview.as_view(), name='reviews'),
    path('subscriptions/', SubscriptionView.as_view(), name='subscriptions'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('members/', CoachView.as_view(), name='members'),
    path('reviews/<int:pk>/delete/', DeleteReview.as_view(), name='delete'),
    path('reviews/<int:pk>/update/', UpdateReview.as_view(), name='update'),
    path('logout/', logout_user, name='logout'),
]
