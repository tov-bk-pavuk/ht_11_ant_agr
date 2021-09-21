import os

from celery import Celery
from celery import shared_task

from datetime import timedelta

from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ht_11_ant_agr.settings')

app = Celery('ht_11_ant_agr')  # редактировать тут было вот это app = Celery('ht_11_ant_agr')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@shared_task
def notify():
    pass


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
