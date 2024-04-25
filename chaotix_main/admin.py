from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(TextToImageAI)
class TextToImageAI(admin.ModelAdmin):
    ordering = ["-modified"]
    list_display = (
        "id",
        "img_text",
        "img_url",
    )
    list_filter = ("img_text", "id")

