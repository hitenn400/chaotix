from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")

base_url = os.environ.get("REDIS_URL", "redis://localhost:6379")

app = Celery("django_celery")

app.conf.enable_utc = False


app.config_from_object(settings, namespace="CELERY")


app.autodiscover_tasks()

app.conf.broker_url = base_url


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
