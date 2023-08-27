class Unidad_tiempo:
    
    def __init__(self):
        self.valor=0
        self.tope=0

    def avanzar(self):
        self.valor += 1
        if self.valor == self.tope:
            self.valor = 0
