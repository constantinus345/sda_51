

#pip install ocrmypdf
#documentatia https://ocrmypdf.readthedocs.io/en/latest/cookbook.html#add-an-ocr-layer-and-convert-to-pdf-a

import ocrmypdf
#Vom adauga un text deasupra  imaginii scanate, astfel incat sa putem cauta in document

pdf_scanat_path = "B:/pyx/SDA/sda_51/sv600_m_automatic.pdf"

pdf_scanat_out = f"{pdf_scanat_path.replace('.pdf', 'OCR.pdf')}"
ocrmypdf.ocr(input_file=pdf_scanat_path,
             output_file=pdf_scanat_out)