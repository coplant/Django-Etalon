from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth import views as auth_views

from main.models import Direction, Schedule, Review, Subscription


# class Login(auth_views.LoginView):


class MainView(TemplateView):
    template_name = 'main/index.html'


class DirectionsView(ListView):
    template_name = 'main/directions.html'
    model = Direction


class ScheduleView(ListView):
    template_name = 'main/schedule.html'
    model = Schedule


class ReviewView(ListView):
    template_name = 'main/reviews.html'
    model = Review
    paginate_by = 10


class SubscriptionView(ListView):
    template_name = 'main/subscriptions.html'
    model = Subscription


def members(request):
    return render(request, template_name='main/members.html', context={})


def user(request):
    return HttpResponse('user')
