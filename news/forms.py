import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import News

from captcha.fields import CaptchaField  # Library which add captcha in project.


class ContactForm(forms.Form):
    """Form which help user sent message for project-team on their e-mail address."""
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    captcha = CaptchaField()  # Show captcha field.


class UserLoginForm(AuthenticationForm):
    """Form for connection(login) user in system."""
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    """Form for register user in system."""
    username = forms.CharField(label='Имя пользователя',
                               help_text='Имя пользователя должно состоять максимум из 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Connect model in class.
        fields = ('username', 'email', 'password1', 'password2',)


class NewsForm(forms.ModelForm):
    """Form for creation news on site."""
    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):  # Check title before add.
        title = self.cleaned_data['title']
        if re.match(r'\d', title):  # Check begin of title on numbers.
            raise ValidationError('Название не должно начинаться с цифры!')
        return title


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=70)
#     content = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'rows': 5,
#     }))
#     category = forms.ModelChoiceField(queryset=News.objects.all())
