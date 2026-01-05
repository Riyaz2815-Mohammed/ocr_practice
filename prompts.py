def document_analysis_prompt(ocr_text: str) -> str:
    return f"""
You are an OCR analysis engine.

Your task is to analyze the OCR-extracted text and return ONLY a Python-style dictionary
that can be directly parsed using json.loads().

STRICT RULES:
- Return ONLY the dictionary.
- Do NOT include explanations.
- Do NOT include markdown or code blocks.
- Do NOT include extra text before or after the dictionary.
- Use double quotes for all strings.
- Ensure valid JSON syntax.

Required dictionary format:

{{
  "document_summary": "<brief explanation of what the document is about>",
  "overall_confidence": <float between 0 and 1>,
  "lines": [
    {{
      "text": "<line text>",
      "confidence": <float between 0 and 1>,
      "low_confidence": <true or false>
    }}
  ]
}}

OCR Text:
{ocr_text}
"""
