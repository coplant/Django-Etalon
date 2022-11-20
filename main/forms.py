from django import forms
from django.contrib.auth import validators
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.password_validation import validate_password

from .models import User
from django.core.exceptions import ValidationError


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'form-input form-control', 'placeholder': 'Логин', 'autocomplete': 'new-password'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input form-control', 'placeholder': 'Пароль', 'autocomplete': 'new-password'}))
    password2 = forms.CharField(label='Пароль (подтверждение)', widget=forms.PasswordInput(
        attrs={'class': 'form-input form-control', 'placeholder': 'Пароль (подтверждение)', 'autocomplete': 'new-password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 4:
            raise ValidationError('Имя пользователя слишком короткое.')
        if len(username) > 20:
            raise ValidationError(f'Имя пользователя слишком длинное. Убедитесь, что значение содержит не более 20 '
                                  f'символов. ( Сейчас {len(username)}).')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Это имя пользователя уже занято. Попробуйте другое.')
        return username

    def clean_password(self):
        password = self.cleaned_data['password1']
        validate_password(password)
        return password

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('Пароль не совпадает.')
        return data['password2']

    def is_valid(self):
        result = super().is_valid()
        for x in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[x].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result
