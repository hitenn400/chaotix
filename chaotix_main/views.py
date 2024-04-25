from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from chaotix_main import signals
from .models import TextToImageAI
from chaotix.utils.helper import describe_exception
from django.core.exceptions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import TextToImageAISerializer

# Create your views here.
class TestEndpoint(APIView):
    permission_classes = []  # disables permission

    def get(self, request):
        try:
            return Response({"Ping": "Pong!"})
        except Exception as e:
            print(describe_exception(e))

class TextToImageGenerator(APIView):
    permission_classes = []  # disables permission

    def post(self, request):
        try:
            payload = request.data
            cfg_scale = request.data.get("cfg_scale",None)
            height = request.data.get("height",None)
            width = request.data.get("width",None)
            sampler = request.data.get("sampler",None)
            samples = request.data.get("samples",None)
            steps = request.data.get("steps",None)
            weight = request.data.get("weight",None)
            meta_info = {
                "cfg_scale":cfg_scale,
                "height":height,
                "width":width,
                "sampler":sampler,
                "samples":samples,
                "steps":steps,
                "weight":weight
            }
            text_prompts = request.data.get("text_prompts",[])
            for text in text_prompts:
                text_to_image_obj = TextToImageAI.objects.create(img_text=text,display_img_text=text,meta_info=meta_info)
                signals.image_generator_signal(text_to_img_id=text_to_image_obj.id)
                
            response_dict = {
                "custom_status_code": 0,
                "status_msg": "Image generation is in progress!",
                "data_dict": {},
            }   

            return Response(
                response_dict
            )  
        except Exception as e:
            print("Exception occured in class TextToImageGenerator:POST ",describe_exception(e))
            response_dict = {
                "custom_status_code": -1,
                "status_msg": "Something went wrong",
                "data_dict": {"error_msg":str(e)},
            }   
            return Response(response_dict)


class TextToImageList(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = TextToImageAISerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = [
        "id", "img_text"
    ]
    search_fields = [
        "img_text"
    ]

    def get_queryset(self):
        results = TextToImageAI.objects.all().order_by("-modified")
        return results

    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(TextToImageList, self).list(request, *args, **kwargs)

        response_dict = {
            "custom_status_code": 0,
            "status_msg": "Lead list fetch successful",
            "data_dict": response.data,
        }
        return Response(response_dict)