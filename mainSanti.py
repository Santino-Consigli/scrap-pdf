import fitz
import os
import re
from medicamento import *
from encabezado import *

# leer pdf de la carpeta input
pdf = fitz.open("input/FORMULARIO A.pdf")

# for pagina in range(1):
#     pagina_actual = pdf[pagina]
#     texto = pagina_actual.get_text()
#     print(texto)


pag = pdf.load_page(0)
texto = pag.get_text().split('\n')

dicionarioClaveValorColumnas = {
    1: 'stock_inicial',
    2: 'unidades_CSL',
    3: 'unidades_recibidas',
    4: 'UnEnt',
    5: 'otras_salidas_NoApto',
    6: 'otras_salidas',
    7: 'ajuste',
    8: 'stock_final'
}


def extract_header(texto):
    ##todo refactor to use regex, dont works in pdfs B
    word = "Final"
    textoEncabezado = ''
    indexToMedicamentos = 0
    for index, linea in enumerate(texto):
        if word in linea:
            indexToMedicamentos = index
            break
        else:
            textoEncabezado += linea + '\n'
    nuevoEncab = Encabezado(texto[0][22:], texto[1][7:], texto[2][19:], texto[3][21:], texto[4][17:-1], texto[5][26:],
                            texto[6][11:], texto[7][20:])
    return nuevoEncab, indexToMedicamentos


def extract_medications(texto, start_index):
    ##todo see how to extract code and description in two cells
    textoMedicamentos = '\n'.join(texto[start_index + 1:])
    regexCodeMedication = r'^\d{3} '
    previous_line = ''
    lineaToSave = ''
    contadorColumnas = 1
    medicamentos = []
    stock_values = []
    for linea in textoMedicamentos.split('\n'):
        if re.match(regexCodeMedication, previous_line) and not re.match(regexCodeMedication, linea) and len(linea) > 2:
            lineaToSave = previous_line + ' ' + linea
        else:
            if re.match(regexCodeMedication, linea):
                lineaToSave = linea
            else:
                ## si no es una linea que cumpla ni el regex del codigo de medicacion, ni es una linea larga, entonces es una linea de valores
                ##sabemos que siempre van a ser 9 columnas
                for x in range(1, 9):
                    if contadorColumnas == x:
                        stock_values.append(linea)
                        contadorColumnas += 1
                        break
                if contadorColumnas == 9:
                    medicamento = Medicamento(lineaToSave, stock_values[0], stock_values[1], stock_values[2],
                                              stock_values[3], stock_values[4], stock_values[5], stock_values[6],
                                              stock_values[7])
                    medicamentos.append(medicamento)
                    contadorColumnas = 1
                    stock_values = []
        previous_line = linea
    for medicamento in medicamentos:
        print(medicamento.toString())


def getData():
    nuevoEncab, indexToMedicamentos = extract_header(texto)
    print(nuevoEncab.toString())
    extract_medications(texto, indexToMedicamentos)


if __name__ == "__main__":
    os.system('cls')
    getData()

