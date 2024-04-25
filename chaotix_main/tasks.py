from pathlib import Path
import tempfile
from integrations.stabilityAI.stabilityAI_wrapper import *

from config import celery_app



@celery_app.task()
def image_generator_task(text_to_img_id):
    try:
        stability_wrapper = StabilityAIWrapper(mode="PROD")
        response = stability_wrapper.generate_image_from_text(text_to_img_id=text_to_img_id)
        temp_dir = tempfile.TemporaryDirectory()
        download_file_path = Path(temp_dir.name)
        res,path = base64_to_image_and_save(base64_string=response['artifacts'][0]['base64'],directory_path=temp_dir,filename=f"{text_to_img_id}.png")
        
    except Exception as e:
        print("Exception occured in image_generator_task: ",str(e))