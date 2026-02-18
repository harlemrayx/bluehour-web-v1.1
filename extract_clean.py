from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

pdf_path = r"d:\myproj\bluehourproj\Blue Hour Project Documentation.md.pdf"

try:
    # Try with raw order (no layout analysis)
    text = extract_text(pdf_path, laparams=None)
    print("--- RAW CONTENT START ---")
    print(text)
    print("--- RAW CONTENT END ---")
except Exception as e:
    print(f"Error reading PDF: {e}")
