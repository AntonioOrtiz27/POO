from classServicio import Servicio
class Premium(Servicio):
    __precio_barra:int
    __precio_copetin:int
    __tipo_copetin:str

    def __init__(self,iluminacion,sonido,precioBarra,precioCopetin,copetin):
        super().__init__(iluminacion,sonido)
        self.__precio_barra = precioBarra
        self.__precio_copetin= precioCopetin
        self.__tipo_copetin = copetin

    def getPrecio(self):
        return self.__precio_barra
    def getPrecioCopetin(self):
        return self.__precio_copetin
    def getCopetin(self):
        return self.__tipo_copetin
    
    def __str__(self):
        return super().__str__() + f"Tipo de servicio: Premium | Precio barra: {self.__precio_barra} | Precio Copetin: {self.__precio_copetin} | Tipo copetin: {self.__tipo_copetin}"
    
    def importe(self):
        precio = 0
        precio = (self.getIluminacion() + self.getSonido() + self.__precio_barra + self.__precio_copetin)
        return precio