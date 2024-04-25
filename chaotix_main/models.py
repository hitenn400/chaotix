from django.db import models
from django.db.models import *
from django_extensions.db.models import TimeStampedModel
from shortuuid.django_fields import ShortUUIDField

from .model_helpers import TextToImageAIMixin
# Create your models here.
class TextToImageAI(TextToImageAIMixin,TimeStampedModel, models.Model):
    id = ShortUUIDField(
        length=8,
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        primary_key=True,
        editable=False,
    )
    img_text = models.TextField()
    display_img_text = models.TextField()
    img_url = models.JSONField(default={}, blank=True, null=True)
    meta_info = models.JSONField(default={}, blank=True, null=True)
    class Meta:
        db_table = "text_to_image_ai"
        get_latest_by = "modified"

    def __str__(self):
        return str(self.id)
