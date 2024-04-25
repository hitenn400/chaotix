import cloudinary
import os
from chaotix.utils.helper import describe_exception
from chaotix_main.models import TextToImageAI
from django.core.exceptions import *
from dotenv import load_dotenv

load_dotenv()
import cloudinary.uploader

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)


def upload_img(file_path, id):
    try:
        try:
            text_to_image_obj = TextToImageAI.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Exception("TextToImageAI does not exist for given id: ", id)
        cloudinary_res = cloudinary.uploader.upload(file=file_path, public_id=id)
        if "public_id" in cloudinary_res:
            text_to_image_obj.img_url = cloudinary_res["url"]
            text_to_image_obj.save()
        return True
    except Exception as e:
        print("Exception occured in upload_img :", describe_exception(e))
        raise e
