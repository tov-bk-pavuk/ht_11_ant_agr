from django import forms


class Notification(forms.Form):
    email = forms.EmailField(label='E-Mail')
    text = forms.CharField(label='текст напоминания', max_length=100)
    datetime = forms.DateTimeField()
