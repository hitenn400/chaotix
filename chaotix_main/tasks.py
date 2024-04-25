from pathlib import Path
import tempfile
from chaotix.utils.img_uploader import upload_img
from integrations.stabilityAI.stabilityAI_wrapper import *

# from config import celery_app


# @celery_app.task()
def image_generator_task(text_to_img_id):
    try:
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
            return upload_img(file_path=path, id=text_to_img_id)
        return False
    except Exception as e:
        print("Exception occured in image_generator_task: ", str(e))
