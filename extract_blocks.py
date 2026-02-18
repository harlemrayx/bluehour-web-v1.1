from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LAParams

pdf_path = r"d:\myproj\bluehourproj\Blue Hour Project Documentation.md.pdf"

try:
    laparams = LAParams()
    for page_layout in extract_pages(pdf_path, laparams=laparams):
        # Collect all text containers
        elements = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                elements.append(element)
        
        # Sort by vertical position (top to bottom), then horizontal (left to right)
        # origin is bottom-left, so higher y is higher on page
        elements.sort(key=lambda b: (-b.y1, b.x0))
        
        print(f"--- PAGE START ---")
        for e in elements:
            print(e.get_text().strip())
            print("-" * 20)
        print(f"--- PAGE END ---")

except Exception as e:
    print(f"Error reading PDF: {e}")
