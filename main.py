from cronometro import Cronometro


c=Cronometro()

while c.Hora.valor < 24:
    c.avanzar()
    print(c.Hora.valor , c.Minuto.valor , c.Segundo.valor)