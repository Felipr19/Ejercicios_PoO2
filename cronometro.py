from Hora import Hora
from Minuto import Minuto
from Segundo import Segundo


class Cronometro():
    def __init__(self) -> None:
        self.Hora=Hora()
        self.Segundo=Segundo()
        self.Minuto=Minuto()
    
    def avanzar(self):
        self.Segundo.avanzar()
        if self.Segundo.valor == 0:
            self.Minuto.avanzar()
            if self.Minuto.valor == 0:
                self.Hora.avanzar()
                