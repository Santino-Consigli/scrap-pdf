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
    print("probando")
    print(texto[0][22:])
    print(texto[1][7:])
    print(texto[2][19:])
    print(texto[3][21:])
    print(texto)

    #cargar en la clase encabezado

    #nuevoEncab = Encabezado()
    #nuevoEncab.numForm = texto[18:]
    # fecha
    # respCarga
    # numDoc
    # establecimiento
    # fechaFormu
    # consultas
    # recetas

    #crgar medicamentos, recorro con ciclo ford
    
    

if __name__ == "__main__":
    os.system('cls')
    print(texto)
    getData()
