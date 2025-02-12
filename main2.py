import fitz
import os
import re
from medicamento import *
from encabezado import * 
#leer pdf de la carpeta input
pdf = fitz.open("input/FORMULARIO A.pdf")

# for pagina in range(1):
#     pagina_actual = pdf[pagina]
#     texto = pagina_actual.get_text()
#     print(texto)
    
          
pag = pdf.load_page(0)
texto = pag.get_text().split('\n')



def extractEncabezado(texto):
    word = "Final"
    textoEncabezado = ''
    indexToMedicamentos = 0
    for index, linea in enumerate(texto):
        if word in linea:
            indexToMedicamentos = index
            break
        else:
            textoEncabezado += linea + '\n'
    return textoEncabezado, indexToMedicamentos

def getTextoMedicamentos():
    textoEncabezado, indexToMedicamentos = extractEncabezado(texto)
    textoMedicamentos = ""
    for index in range(indexToMedicamentos + 1, len(texto)):
        textoMedicamentos += texto[index] + '\n'
    return textoMedicamentos


def validateIfRegex(palabra):
    regexCodeMedication = r'^\d{3} '
    if re.findall(regexCodeMedication, palabra):
     return True


if __name__ == "__main__":
    os.system('cls')
    textoMedicamentos= getTextoMedicamentos()
    counter=0
    listaMedicamentos =[]
    newMedicamento = []
    for palabra in textoMedicamentos.split('\n'):
        counter+=1

        if counter ==1 and validateIfRegex(palabra):
            print("crear nuevo medicamento")

        else:





         if counter==10:
              counter=0




