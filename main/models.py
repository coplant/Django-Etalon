from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


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
        return f'{self.author}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['date']


class Subscription(models.Model):
    TIME_OF_DAY = [
        ('0', 'Утро'),
        ('1', 'Вечер')
    ]
    time = models.CharField(max_length=1, choices=TIME_OF_DAY, verbose_name='Время')
    sessions = models.IntegerField(blank=True, verbose_name='Количество')
    price = models.IntegerField(verbose_name='Стоимость')

    def __str__(self):
        return f'{self.time} - {self.sessions} занятий - {self.price}'

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
    DAYS_OF_WEEK = [
        ('1', 'Понедельник'),
        ('2', 'Вторник'),
        ('3', 'Среда'),
        ('4', 'Четверг'),
        ('5', 'Пятница'),
        ('6', 'Суббота'),
        ('0', 'Воскресенье'),
    ]
    direction = models.ForeignKey('Direction', on_delete=models.CASCADE, verbose_name='Направление')
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK, verbose_name='День недели')
    time = models.TimeField(verbose_name='Время')

    def __str__(self):
        return self.direction.title

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
