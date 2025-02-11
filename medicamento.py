class Medicamento:
 
    def __init__(self, descripcion, stock_inicial, unidades_CSL, unidades_recibidas, UnEnt, otras_salidas_NoApto, otras_salidas, ajuste, stock_final):
        self.descripcion = descripcion
        self.stock_inicial = stock_inicial
        self.unidades_CSL = unidades_CSL
        self.unidades_recibidas = unidades_recibidas
        self.UnEnt = UnEnt
        self.otras_salidas_NoApto = otras_salidas_NoApto
        self.otras_salidas = otras_salidas
        self.ajuste = ajuste
        self.stock_final = stock_final
