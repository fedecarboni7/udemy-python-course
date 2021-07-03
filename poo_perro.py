from datetime import date

def calculate_age(anio, mes, dia):
    today = date.today()
    return today.year - anio - ((today.month, today.day) < (mes, dia))

class Perro:
    hambre = True

    def __init__(self, nombre = None, raza = None, fecha_de_nacimiento = None):
        self.nombre = nombre
        self.raza = raza
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.edad = None
        print("Se encontró un perro.\n")

    def nombrar(self):
        self.nombre = input("¿Cómo lo vas a llamar?\n")

    def definir_raza(self):
        self.raza = input("¿De qué raza es?\n")

    def calcular_edad(self):
        self.fecha_de_nacimiento = input("Ingresa la fecha de nacimiento (dd/mm/aaaa)\n")
        dia, mes, anio = self.fecha_de_nacimiento.split("/")
        self.edad = calculate_age(int(anio), int(mes), int(dia))

    def alimentar(self):
        self.hambre = False
        print("Guau guau, gracias")

def main():
    print("\nPrograma para tener un perro:")
    perro = Perro()
    print("Para conocer el estado de tu perro, ingresa alguna de las siguientes opciones:")
    opcion = int(input("1. Nombre\n2. Edad\n3. Raza\n4. Hambre\n5. Salir\nIngresar opción: "))
    while opcion != 5:
        if opcion == 1:
            if perro.nombre == None:
                perro.nombrar()
            else:
                print(perro.nombre)
        elif opcion == 2:
            if perro.edad == None:
                perro.calcular_edad()
            else:
                print(perro.edad, "años")
        elif opcion == 3:
            if perro.raza == None:
                perro.definir_raza()
            else:
                print(perro.raza)
        elif opcion == 4:
            if perro.hambre:
                print("\nTu perro tiene hambre.")
                opcion = int(input("Presioná 1 para alimentarlo, o 0 para no\n"))
                if opcion == 1:
                    perro.alimentar()
                elif opcion == 0:
                    print("Acordate de darle comida después")
                else:
                    print("Tenías que tocar 0 o 1")
            else:
                print("Sin hambre por ahora.")
        opcion = int(input("\n1. Nombre\n2. Edad\n3. Raza\n4. Hambre\n5. Salir\nIngresar opción: "))
    print("\nNos vemos che")
    

main()