from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

pdf_path = r"d:\myproj\bluehourproj\Blue Hour Project Documentation.md.pdf"

try:
    # Try with layout analysis
    laparams = LAParams()
    text = extract_text(pdf_path, laparams=laparams)
    print("--- CONTENT START ---")
    print(text)
    print("--- CONTENT END ---")
except Exception as e:
    print(f"Error reading PDF: {e}")
