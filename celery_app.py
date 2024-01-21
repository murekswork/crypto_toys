import logging
import os
import time
from datetime import datetime

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


# This dictionary creates tasks that calls
# function  @upload_coingecko_data every 10 minutes
app.conf.beat_schedule = {'run-every-1-minute':
                              {
                                'task': 'main.tasks.upload_coingecko_data',
                                'schedule': 600.0,
                              }
                          }
