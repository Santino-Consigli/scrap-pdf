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

#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#       LEER ENCABEZADO
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# funcion para convertir a entero, rama verdadera devuelve el entero, rama falsa devuelve un falso bool


    def convertir_a_entero(cadena):
        try:
            return int(cadena)
        except ValueError:
            return False
        
    documento = texto[3][21:]

    if  convertir_a_entero(documento):
        nuevoEncab = Encabezado(texto[0][22:], texto[1][7:],texto[2][19:],documento, texto[4][17:-1], texto[5][26:], texto[6][11:], texto[7][20:])
    else:
        nuevoEncab = Encabezado(texto[0][22:], texto[1][7:],texto[2][19:]+ " " +texto[3],texto[4][21:], texto[5][17:-1], texto[6][26:], texto[7][11:], texto[8][20:])

    print(nuevoEncab.toString())
    print("- - - - - - - - -")

    
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#       LEER DATOS
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    array_datos = 10 * [None]
    count = 0
    final_true = False


        
    def validar_codigo_datos(codigo):
        if len(codigo) > 3:  # Verificar que la longitud sea suficiente
            if codigo[:3].isdigit():
                if codigo[3] == " ":
                    # print("Ves un espacio, yeyy")
                    return True
                else:
                    print("No validado el código: el quinto carácter no es un espacio.")
                    return False
            else:
                print("No es código, siguiente")
                return False
        else:
            # print("Código demasiado corto")
            return False

    for i in texto:
        if final_true:
            if count < 10:
                if count == 0:
                    if validar_codigo_datos(i):
                        array_datos[count] = i 
                        count += 1
                elif count == 1:
                    if i.isdigit() == False:
                        array_datos[count-1] = array_datos[count-1] + " " + i
                    else:
                        array_datos[count] = i 
                        count += 1
                else:
                    array_datos[count] = i 
                    count += 1
            else:
                count = 0
                # print(" - - - - - - - - - - - - - ")
                # print("Array datos capturados")
                print(" - - - - - - - - - - - - - ")
                print(array_datos)
                print(" - - - - - - - - - - - - - ")
        else:
            if i == "Final":
                print("Llegue a la palabra Final")
                final_true = True

                




#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    os.system('cls')
    # print(texto)
    print("- - - - Obtener data - - - - ")
    getData()