from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('main')


def directions(request):
    return HttpResponse('directions')


def schedule(request):
    return HttpResponse('schedule')


def subscriptions(request):
    return HttpResponse('subscriptions')


def members(request):
    return HttpResponse('members')


def reviews(request):
    return HttpResponse('reviews')
