pdf_path_simplu = "B:/pyx/SDA/sda_51/abc.pdf"

#pip install PyPDF2
import PyPDF2

def citire_pdf(path_pdf):
    #Deschid fisierul in modul de citire binary "rb"
    with open(path_pdf, "rb") as file:
        #creez un obiect de citire a pdf
        reader = PyPDF2.PdfReader(file)

        #gasesc cate pagini are fisierul meu pdf
        num_pages = len(reader.pages)

        #iterez pe fiecare pagina si imi extrag textul
        text = ""
        for p in range(num_pages):
            pagina = reader.pages[p]
            text += pagina.extract_text()

    return text

print(citire_pdf(pdf_path_simplu))

alt_pdf = "B:/pyx/SDA/sda_51/sv600_m_automaticOCR.pdf"

print(citire_pdf(alt_pdf))