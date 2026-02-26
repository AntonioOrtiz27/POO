from classReserva import Reserva
class Nodo:
    __siguiente:object
    __servicio:Reserva

    def __init__(self,NuevaReserva:Reserva):
        self.__siguiente = None
        self.__servicio = NuevaReserva

    def getDato(self): return self.__servicio
    def getSiguiente(self): return self.__siguiente
    def setSiguiente(self,x): self.__siguiente = x