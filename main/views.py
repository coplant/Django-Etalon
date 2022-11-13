from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import views as auth_views

# class Login(auth_views.LoginView):


def index(request):
    # username = 'admin'
    # password = '12345'
    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     print('success')
    return render(request, template_name='main/index.html', context={})


def directions(request):
    return render(request, template_name='main/directions.html', context={})


def schedule(request):
    return render(request, template_name='main/schedule.html', context={})


def subscriptions(request):
    return render(request, template_name='main/subscriptions.html', context={})


def members(request):
    return render(request, template_name='main/members.html', context={})


def reviews(request):
    return render(request, template_name='main/reviews.html', context={})


def user(request):
    return HttpResponse('user')
