from abc import ABC,abstractmethod
class Servicio(ABC):    
    __precio_iluminacion:float
    __precio_sonido:float

    def __init__(self,iluminacion,sonido):
        self.__precio_iluminacion = iluminacion
        self.__precio_sonido = sonido

    def __str__(self):
        return f"""
                Precio Iluminacion: {self.__precio_iluminacion} 
                Precio Sonido: {self.__precio_sonido}
                """    

    def getSonido(self):
        return self.__precio_sonido
    def getIluminacion(self):
        return self.__precio_iluminacion
    
    @abstractmethod
    def importe(self):
        pass
    