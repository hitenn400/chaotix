import base64
import json
import os

import requests
from textImage.utils.helper import describe_exception
from dotenv import load_dotenv

load_dotenv()
import os
from .stabilityAI_constants import *


class StabilityAIException(Exception):
    def __init__(self, id, message, name):
        self.id = id
        self.message = message
        self.name = name

    def __str__(self):
        return self.message


class StabilityAIBase:
    def get_stability_header(self, mode):
        if mode == "TEST":
            api_key = os.getenv("TEST_STABILITY_API_KEY")
        elif mode == "PROD":
            api_key = os.getenv("PROD_STABILITY_API_KEY")
        else:
            raise Exception("mode should be specified as 'PROD','TEST'")
        return api_key


class StabilityAI(StabilityAIBase):
    def __init__(self, mode):
        self.mode = mode
        if mode == "TEST":
            self.api_url = STABILITY_AI_URL["TEST"]
            self.engine_id = STABILITY_ENGINE_ID["TEST"]
        elif mode == "PROD":
            self.api_url = STABILITY_AI_URL["PROD"]
            self.engine_id = STABILITY_ENGINE_ID["PROD"]

    def text_to_image(self, payload_data):
        try:
            url = f"{self.api_url}/{self.engine_id}/text-to-image"
            payload = json.dumps(payload_data)

            auth_header = self.get_stability_header(mode=self.mode)
            headers = {"Content-Type": "application/json", "authorization": auth_header}
            response = requests.post(url, data=payload, headers=headers)
            response_dict = response.json()
            if response.status_code != 200:
                raise StabilityAIException(
                    id=response_dict["id"],
                    message=response_dict["message"],
                    name=[response_dict["name"]],
                )
            return response_dict
        except Exception as e:
            print(
                "Exception occured in class StabilityAI : text_to_image ",
                describe_exception(e),
            )
            raise e
