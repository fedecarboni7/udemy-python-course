#Definiendo un valor predeterminado para el parámetro.
def suma(a = None, b = None):
    if a == None or b == None:
        print("Error, enviar dos números a la función")
    else:
        return a + b

print(suma(2,3))

def duplicar_seq(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2
    return numeros

lista_a = list(range(1,6))
lista_b = duplicar_seq(lista_a)#Argumento por referencia: La lista_a es modificada de su original.
lista_c = list(range(6,11))
lista_d = duplicar_seq(lista_c[:])#Usamos el slicing para no modificar la lista original.

print(lista_a, lista_b, lista_c, lista_d)