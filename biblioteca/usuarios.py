carreras = ["ingenieria","licenciatura","comunicacion","filosofia"]
class Usuario:
    
    def __init__(self):
        self.nombre = None

    def pedir_libro(self):
        pass

    def devolver_libro(self):
        pass

class Estudiante(Usuario):

    def __init__(self):
        self.carrera = None

    def leer_usuario(self):
        self.nombre = input("Insertar el nombre del usuario")
        n = input("Carrera: \n1)ingenieria\n2)licenciatura\n3)comunicacion\n4)filosofia\nelige digitando el numero correspondiente")
        self.carrera = carreras[n]

class Docente(Usuario):

    def __init__(self):
        self.carrera = None
    
    def leer_usuario(self):
        self.nombre = input("Insertar el nombre del usuario")
        n = input("Carrera: \n1)ingenieria\n2)licenciatura\n3)comunicacion\n4)filosofia\nelige digitando el numero correspondiente")
        self.carrera = carreras[n]

class Administrativo(Usuario):

    def __init__(self):
        self.sede = None

    def leer_usuario(self):
        self.nombre = input("Insertar el nombre del usuario")
        n = input("Carrera: \n1)ingenieria\n2)licenciatura\n3)comunicacion\n4)filosofia\nelige digitando el numero correspondiente")
        self.carrera = carreras[n]
