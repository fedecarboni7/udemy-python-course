from datetime import date

def calculate_age(anio, mes, dia):
    today = date.today()
    return today.year - anio - ((today.month, today.day) < (mes, dia))

class Perro:

    #Constructor de clase
    def __init__(self, nombre = None, raza = None, fecha_de_nacimiento = None):
        self.nombre = nombre
        self.raza = raza
        self.fecha_de_nacimiento = fecha_de_nacimiento
        dia, mes, anio = self.fecha_de_nacimiento.split("/")
        self.edad = calculate_age(int(anio), int(mes), int(dia))
        print("Se encontró un perro.\n")

    #Método str()
    def __str__(self):
        return f"Tu perro se llama {self.nombre}, es un {self.raza}, tiene {self.edad} años y nació el {self.fecha_de_nacimiento}"

    #Método len()
    def __len__(self):
        return self.edad
    
    #Destructor de clase
    def __del__(self):
        return f"{self.nombre} se perdió :("

odi = Perro("Odi", "Chihuahua", "01/08/2009")
print(str(odi))
print(len(odi))
del(odi)

