from celery import Celery, shared_task
from django.core.mail import send_mail


@shared_task
def notify(massage, email, datetime):
    delay = datetime  # Задержка отправки 2021-09-22 04:40
    from_email = 'mymail@gmail.com'
    subject = 'Notification'
    recipient_list = email
    send_mail(subject, massage, from_email, [recipient_list])

