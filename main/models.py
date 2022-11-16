from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext as _
from django import forms


class User(AbstractUser):
    photo = models.ImageField(upload_to='user/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_coach = models.BooleanField(default=False, verbose_name='Статус тренера')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']


class Review(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Автор')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    content = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return f'{self.author.first_name} {self.author.last_name}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['date']


class Subscription(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(verbose_name='Содержание')
    price = models.IntegerField(verbose_name='Стоимость')
    photo = models.ImageField(upload_to='subscription/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"


class Direction(models.Model):
    title = models.CharField(max_length=150, verbose_name='Направление')
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='direction/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Schedule(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье'),
    )
    direction = models.ForeignKey('Direction', on_delete=models.CASCADE, verbose_name='Направление')
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK, verbose_name='День недели')
    time = models.TimeField(verbose_name='Время')

    def __str__(self):
        return self.direction.title

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
