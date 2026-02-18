from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LAParams

pdf_path = r"d:\myproj\bluehourproj\Blue Hour Project Documentation.md.pdf"

try:
    laparams = LAParams() # Default params
    for i, page_layout in enumerate(extract_pages(pdf_path, laparams=laparams)):
        print(f"--- PAGE {i+1} ---")
        elements = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                elements.append(element)
        
        # Sort by Y (top to bottom)
        elements.sort(key=lambda b: -b.y1)
        
        for e in elements:
            print(f"[Y={e.y1:.2f}, X={e.x0:.2f}] {e.get_text().strip()[:50]}...")
            
except Exception as e:
    print(f"Error reading PDF: {e}")
