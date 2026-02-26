class Salon():
    __nom_salon:str
    __direccion:str
    __precio_alquiler:int

    def __init__(self,nom,direccion,precio):
        self.__nom_salon = nom
        self.__direccion = direccion
        self.__precio_alquiler = precio

    def __str__(self):
        return f"{self.__nom_salon} | {self.__direccion} | {self.__precio_alquiler}"
    
    def getNombreSalon(self): return self.__nom_salon
    def getDireccion(self): return self.__nom_salon
    def getPrecio(self): return self.__precio_alquiler
