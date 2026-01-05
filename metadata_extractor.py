# metadata_extractor.py

from datetime import datetime

def extract_metadata(analysis_json: dict) -> dict:
    # ----------------------------
    # Direct access (fail fast)
    # ----------------------------
    document_summary = analysis_json["document_summary"]
    overall_confidence = float(analysis_json["overall_confidence"])
    lines = analysis_json["lines"]

    low_confidence_lines = []

    for idx, line in enumerate(lines, start=1):
        if line["low_confidence"] is True:
            low_confidence_lines.append({
                "line_number": idx,
                "text": line["text"],
                "confidence": float(line["confidence"])
            })

    metadata = {
        "document_summary": document_summary,
        "overall_confidence": overall_confidence,
        "total_lines": len(lines),
        "low_confidence_count": len(low_confidence_lines),
        "low_confidence_lines": low_confidence_lines
    }

    # ----------------------------
    # Logging to log.txt
    # ----------------------------
    log_entry = f"\n{'='*60}\n"
    log_entry += f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    log_entry += f"Total Lines: {metadata['total_lines']}\n"
    log_entry += f"Overall Confidence: {metadata['overall_confidence']}\n"
    log_entry += f"Low Confidence Count: {metadata['low_confidence_count']}\n"
    log_entry += f"Document Summary: {metadata['document_summary'][:100]}...\n"

    if low_confidence_lines:
        log_entry += "Low Confidence Lines:\n"
        for line in low_confidence_lines:
            log_entry += (
                f"  Line {line['line_number']}: "
                f"{line['text'][:80]}... "
                f"(confidence: {line['confidence']})\n"
            )

    log_entry += f"{'='*60}\n"

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)

    return metadata
