class Perro:
    hambre = True

    def __init__(self):
        print("Se encontró un perro.")

    def alimentar(self):
        self.hambre = False

def main():
    print("Programa para tener un perro")
    odi = Perro()
    odi.raza = "Chihuahua"
    odi.edad = 12
    odi.nombre = "Odi"
    print("Podes chequear las siguientes cosas para conocer el estado de tu perro:")
    opcion = int(input("1. Raza\n2. Edad\n3. Nombre\n4. Hambre\n5. Salir\nIngresar opción: "))
    while opcion != 5:
        if opcion == 1:
            print(odi.raza)
        elif opcion == 2:
            print(odi.edad, "años")
        elif opcion == 3:
            print(odi.nombre)
        elif opcion == 4:
            print(odi.hambre)
            if odi.hambre:
                print("Tu perro necesita ser alimentado.")
                dar_comida = int(input("Presioná 1 para alimentarlo, o 0 para no."))
                if dar_comida == 1:
                    odi.alimentar()
                elif dar_comida == 0:
                    print("Acordate de darle comida después")
                else:
                    print("Tenías que tocar 0 o 1")
        opcion = int(input("1. Raza\n2. Edad\n3. Nombre\n4. Hambre\n5. Salir\nIngresar opción: "))
    print("Nos vemos che")
    

main()