# image_ocr.py

import json
from utlis import load_api_key, encode_image
from mistral_clent import get_mistral_client
from prompts import document_analysis_prompt
from metadata_extractor import extract_metadata


API_KEY = load_api_key()
client = get_mistral_client(API_KEY)

IMAGE_PATH = "test_images/test2.jpeg"


b64_image = encode_image(IMAGE_PATH)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "image_url",
        "image_url": f"data:image/jpeg;base64,{b64_image}"
    }
)

ocr_text = ocr_response.pages[0].markdown

print("\n--- OCR OUTPUT ---\n")
print(ocr_text)

with open("ocr_output.md", "w", encoding="utf-8") as f:
    f.write(ocr_text)


prompt = document_analysis_prompt(ocr_text)

llm_response = client.chat.complete(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

analysis_raw = llm_response.choices[0].message.content


try:
    analysis_json = json.loads(analysis_raw)
except json.JSONDecodeError:
    print("LLM did not return valid JSON")
    print(analysis_raw)
    exit(1)

metadata = extract_metadata(analysis_json)

print("\n--- METADATA ---\n")
print(f"Summary: {metadata['document_summary']}")
print(f"Overall Confidence: {metadata['overall_confidence']}")
print(f"Total Lines: {metadata['total_lines']}")
print(f"Low Confidence Count: {metadata['low_confidence_count']}")

for line in metadata["low_confidence_lines"]:
    print(
        f"Line {line['line_number']}: "
        f"{line['text']} "
        f"(confidence: {line['confidence']})"
    )
