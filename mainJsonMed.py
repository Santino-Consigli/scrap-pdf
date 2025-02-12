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



def validarID(id):
    if len(id) == 4:
        if id[-1] == ' ':
            return True
        else:
            return False


def getPalabraWithoutNumbers(palabra):
    return palabra[4:]


if __name__ == "__main__":
    os.system('cls')
    textoMedicamentos= getTextoMedicamentos()
    listaMedicamentos =[]
    palabraToComparar = ""
    for palabra in textoMedicamentos.split('\n'):

        if palabra.isnumeric():
            pass
        else:

            if validarID(palabra[:4]):
                medicamento = palabra
                med = Med(palabra[:4],getPalabraWithoutNumbers(palabra))
                listaMedicamentos.append(med)
            else:
                pass

    for med in listaMedicamentos:
        print(med)






