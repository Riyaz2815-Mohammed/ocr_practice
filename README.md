# Image OCR Pipeline (Mistral OCR)

This repository contains an **image-based OCR pipeline** built using the **Mistral OCR API**, designed to extract text from images and generate **structured metadata** such as confidence scores and low-confidence lines.

This module serves as the **foundation layer** for a larger **Document Intelligence / NLP / GenAI system**.


## 🚀 Features

- Supports image inputs (`.jpg`, `.jpeg`, `.png`)
- Converts images to Base64 for OCR processing
- Extracts text using **Mistral OCR**
- Uses an LLM to analyze OCR quality
- Generates structured metadata:
  - Document summary
  - Overall confidence score
  - Line-level confidence
  - Low-confidence line detection
- Logs OCR quality details to a persistent log file


## 🧠 Why This Module Exists

OCR quality directly impacts downstream systems like:
- NLP pipelines
- Document classification
- Semantic comparison (BERT)
- Risk and compliance analysis

This module focuses **only on extraction and quality analysis**, keeping the pipeline:
- Modular
- Explainable
- Industry-aligned


## 📂 Project Structure

# Image OCR Pipeline (Mistral OCR)

This repository contains an **image-based OCR pipeline** built using the **Mistral OCR API**, designed to extract text from images and generate **structured metadata** such as confidence scores and low-confidence lines.

This module serves as the **foundation layer** for a larger **Document Intelligence / NLP / GenAI system**.


## 🚀 Features

- Supports image inputs (`.jpg`, `.jpeg`, `.png`)
- Converts images to Base64 for OCR processing
- Extracts text using **Mistral OCR**
- Uses an LLM to analyze OCR quality
- Generates structured metadata:
  - Document summary
  - Overall confidence score
  - Line-level confidence
  - Low-confidence line detection
- Logs OCR quality details to a persistent log file


## 🧠 Why This Module Exists

OCR quality directly impacts downstream systems like:
- NLP pipelines
- Document classification
- Semantic comparison (BERT)
- Risk and compliance analysis

This module focuses **only on extraction and quality analysis**, keeping the pipeline:
- Modular
- Explainable
- Industry-aligned

## 📂 Project Structure

image_ocr/
│
├── image_ocr.py # Main image OCR pipeline
├── metadata_extractor.py # Extracts confidence metadata and logs results
├── prompts.py # Strict prompt enforcing structured LLM output
├── mistral_client.py # Mistral client wrapper
├── utils.py # API key loader & Base64 encoding
├── ocr_output.md # Raw OCR extracted text
└── log.txt # OCR confidence logs

## ⚙️ Processing Flow
Image
↓
Base64 Encoding
↓
Mistral OCR
↓
Raw OCR Text
↓
LLM-Based OCR Quality Analysis
↓
Metadata Extraction
↓
Confidence Logging

## 🧪 Example Metadata Output

Total Lines: 4
Overall Confidence: 0.85
Low Confidence Count: 1

Low Confidence Line:
"The robaract club of GCT cainbatore organized..."

## 📄 Logging (`log.txt`)

Each execution appends structured logs containing:
- Timestamp
- Total extracted lines
- Overall OCR confidence
- Low-confidence line details

This enables:
- OCR quality monitoring
- Debugging
- Auditability for enterprise systems


## 🔮 Future Extensions

This module is intentionally designed to be extended for:
- PDF OCR (digital & scanned)
- NLP sentence segmentation
- BERT-based semantic similarity
- Document classification
- Clause-level analysis

## 🧑‍💻 Author

Built as part of hands-on learning and development in **OCR, NLP, and GenAI-based document intelligence systems**.

