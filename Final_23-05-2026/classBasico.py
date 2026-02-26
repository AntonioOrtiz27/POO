from classReserva import Reserva
from classServicio import Servicio
class Basico(Servicio):
    __nombre_show:str
    __precio_show:float

    def __init__(self,iluminacion,sonido,nombre,precio):
        super().__init__(iluminacion,sonido)
        self.__nombre_show = nombre
        self.__precio_show = precio

    def getShow(self):
        return self.__nombre_show
    
    def setShow(self,x):
        self.__nombre_show = x

    def setPrecio(self,x):
        self.__precio_show = x
        
    def getPrecio(self):
        return self.__precio_show
    
    def __str__(self):
        return super().__str__() + f"Tipo de servicio: Básico | Nombre: {self.__nombre_show} | Precio: {self.__precio_show}"
    
    def importe(self):
        precio = self.getIluminacion() + self.getSonido() + self.__precio_show
        return precio