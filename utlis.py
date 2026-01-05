# utils.py

import base64

def load_api_key(path: str = "api.txt") -> str:
    with open(path, "r") as f:
        return f.read().strip()

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
