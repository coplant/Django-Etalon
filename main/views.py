from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth import views as auth_views
from django.views.generic.list import MultipleObjectMixin
from django.utils.timezone import utc
from main.forms import RegisterUserForm, LoginUserForm, ReviewForm
from main.models import Direction, Schedule, Review, Subscription, User


# class Login(auth_views.LoginView):


class MainView(TemplateView):
    template_name = 'main/index.html'


class DirectionsView(ListView):
    template_name = 'main/directions.html'
    model = Direction


class ScheduleView(ListView):
    template_name = 'main/schedule.html'
    model = Schedule


class AddReview(MultipleObjectMixin, CreateView):
    form_class = ReviewForm
    template_name = 'main/reviews.html'
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.get_form()
            for item in form:
                print(item)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = User.objects.get(pk=request.user.id)
                obj.date = datetime.utcnow().replace(tzinfo=utc)
                print(obj)
                obj.save()
            else:
                print(form)
        return redirect('reviews')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Review.objects.order_by('-date')
        return super().get_context_data(**kwargs)


class SubscriptionView(ListView):
    template_name = 'main/subscriptions.html'
    model = Subscription


class CoachView(ListView):
    template_name = 'main/members.html'
    model = User

    def get_queryset(self):
        return User.objects.filter(is_coach=True)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
