class Unidad:
    
    def __init__(self):
        self.valor=0
        self.unidad=0

    def avanzar(self):
        self.valor+=1

class binario(Unidad):

    def avanzar(self):
        self.unidad+=1
        self.valor=bin(self.unidad)

class hexal(Unidad):

    def avanzar(self):
        self.unidad+=1
        self.valor=hex(self.unidad)

class octal(Unidad):

    def avanzar(self):
        self.unidad+=1
        self.valor=oct(self.unidad)
