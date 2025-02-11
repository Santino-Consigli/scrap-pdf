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
texto = pag.get_text().split('/n')

def getData():
    for t in texto:
        if t == 'Final':
            print('Hola')
    
    
    

if __name__ == "__main__":
    os.system('cls')
    print(texto)
    
