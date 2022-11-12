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
    return render(request, template_name='main/directions.html', context={'title': 'Эталон', 'request': request.META['HTTP_USER_AGENT']})


def schedule(request):
    return HttpResponse('schedule')


def subscriptions(request):
    return HttpResponse('subscriptions')


def members(request):
    return HttpResponse('members')


def reviews(request):
    return HttpResponse('reviews')


def user(request):
    return HttpResponse('user')
