with open("api.txt","r") as f:
    api_key=f.read().strip()
from mistralai import Mistral
import base64 as b
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = b.b64encode(img_file.read()).decode('utf-8')
    return b64_string
client = Mistral(api_key=api_key)
image_path1 = "test_image.jpeg"
image_path2="aim_procedure.jpeg"
b64_image = encode_image(image_path2)

ocr_response=client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type":"image_url",
        "image_url":f"data:image/jpeg;base64,{b64_image}"

    }

)

print(ocr_response.pages[0].markdown)
with open("read.md","w",encoding="utf-8") as f:
    f.write(ocr_response.pages[0].markdown)                     