from animales import *
from random import choice

class Tienda:
    
    def __init__(self) -> None:
        self.animales=[]

    def agregar_animal(self,Animal):
        self.animales.append(Animal)

    def entregar_animal(self):
        return(choice(self.animales))
