from animales import *
from tienda import *

t=Tienda()

t.agregar_animal(Perro("Golden",3,27))
t.agregar_animal(Gato("Persa",1,9))
t.agregar_animal(Pez("Carpa",7,3.5))
t.agregar_animal(Ave("Loro",4,7.4))

for i in range(4):
    a=t.entregar_animal()
    print(a.saludar(),a.mostrar_info())