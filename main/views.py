from django.shortcuts import render
from django.http import HttpResponse


def index(request):
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
