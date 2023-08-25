from cronometro import Cronometro

def cronometrar(h,m,s):
    c=Cronometro()
    tiempo=h*(60**2)+m*60+s
    for i in range(tiempo) :
        c.avanzar()
        print(f"{c.Hora.valor} : {c.Minuto.valor} : {c.Segundo.valor}")


cronometrar(1,30,0)