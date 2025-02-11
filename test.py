import pdfplumber
import os

# leer pdf de la carpeta input
with pdfplumber.open("input/FORMULARIO B.pdf") as pdf:
    pag = pdf.pages[0]
    texto = pag.extract_text()

if __name__ == "__main__":
    os.system('cls')
    print(texto)