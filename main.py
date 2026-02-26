from gestor import Lista
from classPremium import Premium
from classBasico import Basico
from claseSalon import Salon
from classReserva import Reserva
def menu():
    op = int(input("""
    [0] para salir
    [1] inciso 1
    [2] inciso 2
    [3] inciso 3
    [4] inciso 4 
    [5] inciso 5
    --->"""))
    return op

if __name__ == "__main__":
    lista = Lista()
    op = menu()
    while op != 0:
        if op == 1:
            print("Cargar Reserva")
            cod = int(input("cargar codigo: "))
            nom = input("nombre: ")
            ape = input("apellido: ")
            tel = input("telefono: ")
            fecha = input("fecha: ")
            cant = input("cantidad de personas:")
            print("Cargar Salon")
            nom_salon = input("ingrese nom salon:")
            dire = input("direccion alquiler:")
            precio = int(input("precio alquiler:"))
            salon = Salon(nom_salon,dire,precio)
            tipo = int(input("ingrese tipo de servicio [1]Basico [2]Premium"))
            if tipo == 1:
                print("Cargar Servicio Basico")
                ilu = float(input("ingrese precio iluminacion: "))
                soni = float(input("ingrese precio de sonido: "))
                nom = input("nombre show:")
                pre = int(input("precio show:"))
                servicio = Basico(ilu,soni,nom,pre)
            elif tipo == 2:
                print("Cargar Servicio Premium")
                ilu = float(input("ingrese precio iluminacion: "))
                soni = float(input("ingrese precio de sonido: "))
                precio = int(input("precio barra:"))
                preciocopetin = int(input("precio copetin:"))
                cope = input("tipo copetin(pizza,pollo,empanada):")
                servicio = Premium(ilu,soni,precio,preciocopetin,cope)
            reserva = Reserva(cod,nom,ape,tel,fecha,cant,salon,servicio)
            print("Reserva cargada\n")
            lista.agregar(reserva)
            lista.mostrar()
        elif op == 2:
            lista.test()
        elif op == 3:
            fecha = input("Ingrese fecha: ")
            lista.inciso3(fecha)
        elif op == 4:
            try:
                cod = int(input("ingrese codigo de una reserva:"))
                lista.inciso4(cod)
            except Exception as e:
                print(e)
        elif op == 5:
            try:
                codigo = int(input("ingrese codigo de una reserva:"))
                lista.inciso5(codigo)
            except Exception as e:
                print(e)
        op = menu()

        
