import fitz
import os
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
    # print(len(texto))
    # print("probando")
    # print(texto[0][22:])
    # print(texto[1][7:])
    # print(texto[2][19:])
    # print(texto[3][21:])
    # print(texto[4][17:-1])
    # print(texto[5][26:])
    # print(texto[6][11:])
    # print(texto[7][20:])

    # contador = 9
    # for i in range(len(texto)):
    #     if i > 29:
    #         swithc (contador >= 9):
    #             print("nombremedicamento" + texto[i])
    #         if contador = 8
    #             contador -= 1
            


    #cargar en la clase encabezado

    #pregunto si la celda del documento se puede castear a int, y si no se puede es porque foma parte del nombre-
    if  int(texto[3][21:]):
        nuevoEncab = Encabezado(texto[0][22:], texto[1][7:],texto[2][19:],texto[3][21:], texto[4][17:-1], texto[5][26:], texto[6][11:], texto[7][20:])
    else:
        nuevoEncab = Encabezado(texto[0][22:], texto[1][7:],texto[2][19:]+texto[3],texto[4][21:], texto[5][17:-1], texto[6][26:], texto[7][11:], texto[8][20:])

    print(nuevoEncab.toString())

    #crgar medicamentos, recorro con ciclo ford
    
    

if __name__ == "__main__":
    os.system('cls')
    print(texto)
    print("- - - - Obtener data - - - - ")
    getData()