from django import forms
from django.forms import ModelForm

from . models import Author, Book


class Notification(forms.Form):
    email = forms.EmailField(label='отправить на E-Mail')
    subject = forms.CharField(label='текст напоминания', max_length=100)
    datetime = forms.DateTimeField(label='дата и время напоминания')


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
