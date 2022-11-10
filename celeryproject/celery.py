from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'celeryproject.settings')
app = Celery('celeryproject')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace=' CELERY')

from celery.schedules import crontab

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'send_email_app.task.send_mail_func',
        'schedule': crontab(hour=23, minute=40),
        #'args': (2,)
    }
}
# Celery Beat Settings
app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')