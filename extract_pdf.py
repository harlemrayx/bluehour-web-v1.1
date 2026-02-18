from pdfminer.high_level import extract_text
import glob
import os

pdf_files = glob.glob("*.pdf")
if not pdf_files:
    print("No PDF found.")
    exit(1)

pdf_path = pdf_files[0]
print(f"Reading: {pdf_path}")

try:
    text = extract_text(pdf_path)
    print("--- CONTENT START ---")
    print(text)
    print("--- CONTENT END ---")
except Exception as e:
    print(f"Error reading PDF: {e}")
