import fitz
import os
import re
from medicamento import *
from encabezado import * 
#leer pdf de la carpeta input
pdf = fitz.open("input/FORMULARIO B.pdf")

# for pagina in range(1):
#     pagina_actual = pdf[pagina]
#     texto = pagina_actual.get_text()
#     print(texto)
    
          
pag = pdf.load_page(0)
texto = pag.get_text().split('\n')


def getData():
    word = "Medicamentos"
    textoEncabezado = ''
    textoMedicamentos = ''
    indexToMedicamentos =0
    for index, linea in enumerate(texto):
        if word in linea:
            indexToMedicamentos = index
            print(linea)
            break
        else:
            textoEncabezado += linea + '\n'
            print(textoEncabezado)
    #todoo get data from header with regexs and create instance of Encabezado
    nuevoEncab = Encabezado(texto[0][22:], texto[1][7:],texto[2][19:],texto[3][21:], texto[4][17:-1], texto[5][26:], texto[6][11:], texto[7][20:])
    print(nuevoEncab.toString())

    for index in range(indexToMedicamentos+1, len(texto)):
        textoMedicamentos += texto[index] + '\n'
        #print(textoMedicamentos)
    regexCodeMedication = r'^\d{3} '
    contador = 0
    for linea in textoMedicamentos.split('\n'):
        if re.search(regexCodeMedication, linea):
            
            contador += 1
            print(linea)
            if(contador == 6):
                break


if __name__ == "__main__":
    os.system('cls')
    getData()
    # print(texto)
    # print("- - - - Obtener data - - - - ")
    # getData()
