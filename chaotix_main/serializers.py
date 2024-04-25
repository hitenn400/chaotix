from rest_framework import serializers
from .models import TextToImageAI
class TextToImageAISerializer(serializers.ModelSerializer):
    class Meta:
        model = TextToImageAI
        fields = ["id", "img_text", "img_url", "meta_info"]