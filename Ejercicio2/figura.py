from punto import Punto
from math import pi

class Figura:

    def __init__(self, punto1, punto2):
        self.origen = punto1
        self.fin = punto2
        self.area = 0
        self.perimetro = 0
    
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def informar_popiedades(self):
        print("tipo de figura ",str(type(self)).split(".")[1][:-2])
        print(f"el area es {self.area}")
        print(f"el perimetro es {self.perimetro}")

class Cuadrado(Figura):
    
    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.area = lado * lado
    
    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.perimetro= lado * 4
class Rectangulo(Figura):
    
    def calcular_area(self):
        base = self.origen.calcular_distancia(Punto(self.fin.x , self.origen.y))

class Triangulo(Figura):
    pass

class Circulo(Figura):
    
    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.area = (radio**2) * pi

    def calcular_perimetro(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.perimetro = (radio*2) * pi
