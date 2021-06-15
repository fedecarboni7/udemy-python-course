# los elementos dentro de un conjunto son únicos
# sus elementos no están ordenados

myset = {12, 23, 5, 4, "hola", "hola", 23, 4, 6, 1.3, "auto", -34, False, True}
myset.add("caballo") #agrega elementos

print(type(myset), len(myset), myset)

#repasoxd
tupla = (0, 325, 3, 4, 3, 4, 325)
print(type(tupla), tupla, set(tupla))

lista = [12, 35, "hola", "chau", -56, "hola", -56]
print(type(lista), lista, set(lista))

dicc = {1: "uno", 2:"dos", "postre": "helado", "juego": "amongus"}
print(type(dicc), dicc, dicc["postre"])

string = "hola como andas? esta es una cadena de ejemplo para pasar a conjunto"
print(set(string))
