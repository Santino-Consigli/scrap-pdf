class Medicamento:

    def __init__(self, descripcion, stock_inicial, unidades_CSL, unidades_recibidas, UnEnt, otras_salidas_NoApto,
                 otras_salidas, ajuste, stock_final):
        self.descripcion = descripcion
        self.stock_inicial = stock_inicial
        self.unidades_CSL = unidades_CSL
        self.unidades_recibidas = unidades_recibidas
        self.UnEnt = UnEnt
        self.otras_salidas_NoApto = otras_salidas_NoApto
        self.otras_salidas = otras_salidas
        self.ajuste = ajuste
        self.stock_final = stock_final

    def toString(self):
        return (f"Descripcion: {self.descripcion}, Stock Inicial: {self.stock_inicial}, "
                f"Unidades CSL: {self.unidades_CSL}, Unidades Recibidas: {self.unidades_recibidas}, "
                f"UnEnt: {self.UnEnt}, Otras Salidas No Apto: {self.otras_salidas_NoApto}, "
                f"Otras Salidas: {self.otras_salidas}, Ajuste: {self.ajuste}, "
                f"Stock Final: {self.stock_final}")