from django import forms


class Notification(forms.Form):
    email = forms.EmailField(label='отправить на E-Mail')
    subject = forms.CharField(label='текст напоминания', max_length=100)
    datetime = forms.DateTimeField(label='дата и время напоминания')
