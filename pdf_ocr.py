with open("api.txt","r") as f:
    api_key=f.read().strip()
from mistralai import Mistral
import os
output_dir="pdf_pages"
os.makedirs(output_dir,exist_ok=True)
client=Mistral(api_key=api_key)

upload_pdf=client.files.upload(
    file={
        "file_name":"sample.pdf",
        "content":open("sample.pdf","rb")

    },
    purpose="ocr"
)

signed_url=client.files.get_signed_url(file_id=upload_pdf.id)

ocr_response=client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type":"document_url",
        "document_url":signed_url.url

    }

)

for i, page in enumerate(ocr_response.pages):
    print(f"--- Page {i+1} ---")
    print(page.markdown)

    with open(f"{output_dir}/page_{i+1}.md","w",encoding="utf-8") as f:
        f.write(page.markdown)