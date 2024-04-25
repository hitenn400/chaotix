import os


from celery import Celery


# set the default Django settings module for the 'celery' program.


# Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")

print("BASE_REDIS_URL: ", BASE_REDIS_URL)


app = Celery("chaotix")




app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# celery_beat settings


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
