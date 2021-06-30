from datetime import datetime
from dateutil.relativedelta import relativedelta

class Perro:
    hambre = True

    def __init__(self, nombre = None, raza = None, fecha_de_nacimiento = None):
        self.nombre = nombre
        self.raza = raza
        self.fecha_de_nacimiento = fecha_de_nacimiento
        print("Se encontró un perro.\n")

    def nombrar(self):
        self.nombre = input("¿Cómo lo vas a llamar?\n")

    def definir_raza(self):
        self.raza = input("¿De qué raza es?\n")

    def calcular_edad(self):
        self.fecha_de_nacimiento = input("Ingresa la fecha de nacimiento (dd/mm/aaaa)\n")
        dia, mes, año = self.fecha_de_nacimiento.split("/")
        self.edad = relativedelta(datetime.now(), datetime(int(año), int(mes), int(dia))).years

    def alimentar(self):
        self.hambre = False

def main():
    print("\nPrograma para tener un perro:")
    perro = Perro("Odi", "Chihuahua")
    print("Para conocer el estado de tu perro, ingresa alguna de las siguientes opciones:")
    opcion = int(input("1. Raza\n2. Edad\n3. Nombre\n4. Hambre\n5. Salir\nIngresar opción: "))
    while opcion != 5:
        if opcion == 1:
            print(perro.raza)
            if perro.raza == None:
                perro.definir_raza()
        elif opcion == 2:
            print(perro.edad)
            if perro.edad == None:
                perro.calcular_edad()
        elif opcion == 3:
            print(perro.nombre)
            if perro.nombre == None:
                perro.nombrar()
        elif opcion == 4:
            if perro.hambre:
                print("\nTu perro tiene hambre.")
                dar_comida = int(input("Presioná 1 para alimentarlo, o 0 para no\n"))
                if dar_comida == 1:
                    perro.alimentar()
                elif dar_comida == 0:
                    print("Acordate de darle comida después")
                else:
                    print("Tenías que tocar 0 o 1")
            else:
                print("Sin hambre por ahora.")
        opcion = int(input("\n1. Raza\n2. Edad\n3. Nombre\n4. Hambre\n5. Salir\nIngresar opción: "))
    print("\nNos vemos che")
    

main()