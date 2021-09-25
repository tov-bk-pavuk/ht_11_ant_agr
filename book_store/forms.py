from django import forms
from django.forms import ModelForm

from . models import Author, Store


class Notification(forms.Form):
    email = forms.EmailField(label='отправить на E-Mail')
    subject = forms.CharField(label='текст напоминания', max_length=100)
    datetime = forms.DateTimeField(label='дата и время напоминания')


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'age']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 14 or age > 100:
            raise forms.ValidationError('Врят-ли в таком возрасте пишут книги')
        return age


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
