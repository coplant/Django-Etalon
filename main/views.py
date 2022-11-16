from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth import views as auth_views

from main.models import Direction, Schedule


# class Login(auth_views.LoginView):


class MainView(TemplateView):
    template_name = 'main/index.html'


class DirectionsView(ListView):
    template_name = 'main/directions.html'
    model = Direction


class ScheduleView(ListView):
    template_name = 'main/schedule.html'
    model = Schedule


def subscriptions(request):
    return render(request, template_name='main/subscriptions.html', context={})


def members(request):
    return render(request, template_name='main/members.html', context={})


def reviews(request):
    return render(request, template_name='main/reviews.html', context={})


def user(request):
    return HttpResponse('user')
