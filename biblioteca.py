from libros import Libro
from usuarios import *

class Biblioteca:

    def __init__(self,sede):
        self.sede = sede
        self.libros = []
    
    def prestar_libro(self,usuario,libro):
        usuario.libros.append(self.libros.pop(libro))
        

