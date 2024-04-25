from pathlib import Path
from chaotix.utils.img_uploader import upload_img
from integrations.stabilityAI.stabilityAI_wrapper import *

# from celery import shared_task
from chaotix.celery_app import app as celery_app


# @shared_task(bind=True)
@celery_app.task()
def image_generator_task(text_to_img_id):
    try:
        print("inside image_generator_task")
        stability_wrapper = StabilityAIWrapper(mode="PROD")
        response = stability_wrapper.generate_image_from_text(
            image_text_ai_id=text_to_img_id
        )
        res, path = base64_to_image_and_save(
            base64_string=response["artifacts"][0]["base64"],
            directory_path=f"integrations/temp_files",
            filename=f"{text_to_img_id}.png",
        )
        if res:
            flag = upload_img(file_path=path, id=text_to_img_id)
        print("completing")
    except Exception as e:
        print("Exception occured in image_generator_task: ", str(e))
