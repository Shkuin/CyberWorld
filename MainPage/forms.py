from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ('name', 'email', 'profile_pic')
        exclude = ['players']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите здесь свой псевдоним'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'})
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)
            self.fields['text'].widget.attrs.update({'class': 'form-control'})
