from django.urls import  path
from chaotix_main import views
urlpatterns=[
    path("ping", views.TestEndpoint.as_view(), name="test_endpoint"),
    path("text-to-image-generator",views.TextToImageGenerator.as_view(),name='text-to-image-generator'),
    path("text-to-image-list",views.TextToImageList.as_view(),name='text-to-image-list')
]