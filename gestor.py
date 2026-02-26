from classBasico import Basico
from classPremium import Premium
from claseSalon import Salon
from classServicio import Servicio
from classReserva import Reserva
from nodo import Nodo
class Lista:
    __actual:Nodo
    __cabeza:Nodo
    __indice:int
    __tope:int

    def __init__(self):
        self.__actual = None
        self.__cabeza = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        self.__actual = self.__cabeza
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__cabeza
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            self.__indice+=1
            return dato
        
    def agregar(self,objeto):
        nuevoNodo = Nodo(objeto)
        nuevoNodo.setSiguiente(self.__cabeza)
        self.__cabeza = nuevoNodo
        self.__tope+=1
        print("Se agrego correctamente")
    
    def mostrar(self):
        for servi in self:
            print(servi)

    def test(self):
        salon = Salon("Le parc","Dr.ortega",10000)
        s_Basico = Basico(100,100,"Ciro",100)
        s_Premium = Premium(1000,1000,1000,1000,"empanada")
        reserva1 = Reserva(1,"ortiz","antonio","2645287471","23/02/2026",7,salon,s_Basico)
        reserva2 = Reserva(2,"juan","Fernandez","2654678960","23/03/2026",2,salon,s_Premium)
        self.agregar(reserva1)
        self.agregar(reserva2)
        self.mostrar()

    def inciso3(self,fecha):
        aux = self.__cabeza
        band = False
        while aux is not None and not band:
            reserva = aux.getDato()
            if reserva.getFecha() == fecha:
                servicio = reserva.getServicio()
                if isinstance(servicio,Premium):
                    print(f"""
                        salon: {reserva.getSalon().getNombreSalon()}
                        direccion: {reserva.getSalon().getDireccion()}
                        nom y apellido: {reserva.getNombre()} {reserva.getApellido()}
                        cantidad: {reserva.getCantidad()}
                        Tipo copetin: {reserva.getServicio().getCopetin()}
                        Mesas: {round(reserva.getMesas())}    
                        """)
                elif isinstance(servicio,Basico):
                    print(f"""
                        salon: {reserva.getSalon().getNombreSalon()}
                        direccion: {reserva.getSalon().getDireccion()}
                        nom y apellido: {reserva.getNombre()} {reserva.getApellido()}
                        cantidad: {reserva.getCantidad()}
                        Show: {servicio.getShow()}
                        Mesas: {round(reserva.getMesas())}
                        """)
                band = True
            aux = aux.getSiguiente()

        if not band:
            print("La fecha no se encontro")

    def inciso4(self,cod):
        aux = self.__cabeza
        band = False
        while aux is not None and not band:
            reserva = aux.getDato()
            if reserva.getCodigo() == cod:
                print(f"Importe total:{reserva.ImporteTotal()}")
                band = True
            
            aux = aux.getSiguiente()

        if not band:
            raise Exception(f"No se encontro el codigo {cod} en las reservas")
        
    def inciso5(self,codigo):
        aux = self.__cabeza
        band = False
        while aux is not None and not band:
            reserva = aux.getDato()
            if reserva.getCodigo() == codigo:
                servi = reserva.getServicio()
                if isinstance(servi,Basico):
                    show = input("Ingrese el nuevo nombre de show para modificarlo:")
                    servi.setShow(show)
                    precio = int(input("Ingrese el nuevo precio de show:"))
                    servi.setPrecio(precio)
                    print("Nombre y precio modificados correctamente")
                    self.mostrar()
                else:
                    print(f"el codigo {codigo} es premium")
                band = True
            aux = aux.getSiguiente()

        if not band:
            raise Exception("codigo de la reserva inexistente")
