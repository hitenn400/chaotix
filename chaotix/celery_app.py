from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chaotix.settings")

base_url = os.environ.get("REDIS_URL", "redis://localhost:6379")

app = Celery("chaotix")

app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata", task_serializer="json")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.beat_schedule = {}

app.autodiscover_tasks()

app.conf.broker_url = base_url


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
