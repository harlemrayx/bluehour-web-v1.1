from pdfminer.high_level import extract_text
import re

pdf_path = r"d:\myproj\bluehourproj\Blue Hour Project Documentation.md.pdf"

try:
    text = extract_text(pdf_path)
    print("--- CONTENT START ---")
    print(text)
    print("--- CONTENT END ---")
except Exception as e:
    print(f"Error reading PDF: {e}")
