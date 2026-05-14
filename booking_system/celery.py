# import os
# from celery import Celery

# os.environ.setdefault("DJANGO_SETTINGS_MODULE","business.settings")

# app = Celery("business")

# app.config_from_object('django.conf:settings',namespace='CELERY')
# app.autodiscover_tasks()
# business/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking_system.settings')

app = Celery('booking_system')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()