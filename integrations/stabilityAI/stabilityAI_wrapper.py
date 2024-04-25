import os
from chaotix_main.models import TextToImageAI
from .stabilityAI_main import StabilityAI, StabilityAIException
from dotenv import load_dotenv
from chaotix.utils.image_converter import base64_to_image_and_save

load_dotenv()


class StabilityAIWrapper:
    def __init__(self, mode):
        if mode not in ("PROD", "TEST"):
            raise Exception("mode should be specified as 'PROD','TEST'")
        self.mode = mode
        self.integration_mode = os.getenv("INTEGRATION_MODE")

    def generate_image_from_text(self, image_text_ai_id):
        try:
            text_to_image_obj = TextToImageAI.objects.get(id=image_text_ai_id)
            meta_info = text_to_image_obj.meta_info
            text_to_image_api_payload = {
                "cfg_scale": meta_info["cfg_scale"],
                "height": meta_info["height"],
                "width": meta_info["width"],
                "sampler": meta_info["sampler"],
                "samples": meta_info.get("samples", 1),
                "steps": meta_info["steps"],
                "text_prompts": [
                    {
                        "text": text_to_image_obj.display_img_text,
                        "weight": meta_info["weight"],
                    }
                ],
            }
            stability_ai = StabilityAI(mode=self.integration_mode)
            try:
                text_to_image_res = stability_ai.text_to_image(
                    payload_data=text_to_image_api_payload
                )
                # base64_to_image_and_save(base64_string=text_to_image_res['artifacts'][0]['base64'],directory_path='integrations/stabilityAI',filename="file_1.png")
                return text_to_image_res
            except StabilityAIException as se:
                raise se

        except TextToImageAI.DoesNotExist:
            raise Exception(
                "TextToImageAI does not exist with given id: ", image_text_ai_id
            )

        except Exception as e:
            raise e
