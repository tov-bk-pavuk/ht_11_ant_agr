from celery import shared_task

from django.core.mail import send_mail


@shared_task
def notify(massage, email):
    from_email = 'mymail@gmail.com'
    subject = 'Notification'
    recipient_list = email
    send_mail(subject, massage, from_email, [recipient_list])
