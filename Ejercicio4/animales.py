class Animal:

    def __init__(self,raza,edad,peso) -> None:
        self.raza=raza
        self.peso=peso
        self.edad=edad

    def saludar(self):
        pass

    def mostrar_info(self):
        return(self.raza , self.edad , self.peso)

class Gato(Animal):
    def saludar(self):
        return("miau")

class Pez(Animal):
    def saludar(self):
        return("gluglu")

class Perro(Animal):
    def saludar(self):
        return("guau")

class Ave(Animal):
    def saludar(self):
        return("rua")