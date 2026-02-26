from claseSalon import Salon
from classServicio import Servicio
class Reserva:
    __codigo:int
    __nombre:str
    __apellido:str
    __telefono:str
    __fecha:str
    __cantidadPersonas:int
    __salon:Salon
    __servicio:Servicio

    def __init__(self,cod,nom,ape,telefono,fecha,cant,salon:Salon,servicio:Servicio):
        self.__codigo = cod
        self.__nombre= nom
        self.__apellido = ape
        self.__telefono = telefono
        self.__fecha = fecha
        self.__cantidadPersonas = cant
        self.__salon = salon
        self.__servicio = servicio

    def __str__(self):
        return f"""
            Reserva
            {self.__codigo} | {self.__nombre} | {self.__apellido} | {self.__telefono} 
            {self.__fecha} | {self.__cantidadPersonas}
            Salon:
            {self.__salon}
            Servicio
            {self.__servicio}
            """
    
    def getCodigo(self): return self.__codigo
    def getNombre(self): return self.__nombre
    def getApellido(self): return self.__apellido
    def getTelefono(self): return self.__telefono
    def getSalon(self): return self.__salon
    def getFecha(self): return self.__fecha
    def getCantidad(self): return self.__cantidadPersonas
    def getServicio(self): return self.__servicio
    def getMesas(self):
        return (self.__cantidadPersonas/8*3)
    
    def ImporteTotal(self):
        importeServicio = self.getServicio().importe()
        precioSalon = self.getSalon().getPrecio()
        return (importeServicio + precioSalon)
