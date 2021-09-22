from celery import Celery, shared_task
from django.core.mail import send_mail


@shared_task
def notify(subject, email, datetime):
    delay = datetime  # Задержка отправки 2021-09-22 04:40
    from_email = 'mymail@gmail.com'
    message = 'Сделай борща!'
    recipient_list = email
    send_mail(subject, message, from_email, [recipient_list])

