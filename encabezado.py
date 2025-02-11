class Encabezado:
    def __init__(self, numForm, fecha, respCarga, numDoc, establecimiento, fechaFormu, consultas, recetas):
        self.numForm= numForm
        self.fecha = fecha
        self.respCarga = respCarga
        self.numDoc = numDoc
        self.establecimiento = establecimiento
        self.fechaFormu = fechaFormu
        self.consultas =  consultas
        self.recetas = recetas
    
    def toString(self):
        return " Numero:" + self.numForm + " Fecha:" + self.fecha + " respCarga:" + self.respCarga + " numDoc:" + self.numDoc + " establecimiento:" + self.establecimiento + " fechaFormu:" + self.fechaFormu + " consultas:" + self.consultas + " recetas:" + self.recetas