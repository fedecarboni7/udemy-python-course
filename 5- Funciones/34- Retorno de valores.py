def lista():
    return [1,2,3,4,5]

print(lista()[1:3])

def lista2():
    return "federico", 1999, "Argentina"

nombre, fecha_de_nacimiento, nacionalidad = lista2()

print(f"Me llamo {nombre} soy de {nacionalidad} y nací en el año {fecha_de_nacimiento}")

def lista3():
    return ["nicolas", 2018, "Israel"]

segundo_nombre = lista3()[0]
año = lista3()[1]
pais = lista3()[2]

print(f"Mi segundo nombre es {segundo_nombre} y en {año} viajé a {pais}")
