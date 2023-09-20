with open('Libros.txt','r') as librostxt:
    libros=librostxt.readlines()

class Libro:
    
    def __init__(self):
        self.titulo=None
        self.autor=None
        self.dispo=True
    
    def leer_libro(self,n):
        libro = libros[n].split(',')
        self.titulo = libro[0]
        self.autor = libro[1]

