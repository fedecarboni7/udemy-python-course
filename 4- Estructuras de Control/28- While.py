contador = 0

while contador <= 5:
    contador += 1
    if contador == 5:
        print("Salimos del while cuando contador es igual a", contador)
        break
    print("Contador vale: ", contador)
print(f"Se hicieron {contador} iteraciones.\n")

contador_1 = 0

while contador_1 <= 5:
    contador_1 += 1
    if contador_1 == 5:
        print(f"Salimos del while cuando contador es igual a {contador_1} y continuamos con la que sigue")
        continue
    print("Contador vale: ", contador_1)
print(f"Se hicieron {contador_1} iteraciones.")