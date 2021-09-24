import os


from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ht_11_ant_agr.settings')

app = Celery('ht_11_ant_agr')  # редактировать тут было вот это app = Celery('ht_11_ant_agr')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parse': {
        'task': 'book_store.tasks.scrap',
        'schedule': crontab(minute=0, hour='1,3,5,7,9,11,13,15,17,19,21,23'),
    }
}
