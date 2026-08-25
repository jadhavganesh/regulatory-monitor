from pypdf import PdfReader


def extract_text_from_pdf(pdf_path:str):
    reader = PdfReader(pdf_path)
    pages=[]

    for page_number,page in enumerate(reader.pages,start=1):

        text = page.extract_text()

        if text:
            pages.append(f"\n--- PAGE {page_number} ---\n{text}")


    return "\n".join(pages)