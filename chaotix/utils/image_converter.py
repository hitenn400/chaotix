import base64
import os
from PIL import Image
from io import BytesIO

def base64_to_image_and_save(base64_string,directory_path, filename):
    try:
        # Decode the base64 string
        image_bytes = base64.b64decode(base64_string)
        
        # Convert bytes to image
        image = Image.open(BytesIO(image_bytes))
        
        # Check if the image is PNG format
        if image.format != 'PNG':
            raise ValueError("Input is not a PNG image")
        
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        
        # Save the image to the specified directory
        full_path = os.path.join(directory_path, filename)

        # Save the image to local file
        image.save(full_path, "PNG")
        print("Image saved successfully as", filename)
        return True,full_path
        
    except Exception as e:
        print("Error:", e)

