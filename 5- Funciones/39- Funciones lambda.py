#Hacemos una función cualquiera de manera tradicional
def duplicar(n): return n*2
print(duplicar(4))

#Ahora la hacemos usando lambda
duplico = lambda num: num*2
print(duplico(6))

#Más ejemplos
impar = lambda num: num%2 != 0
print(impar(3))

revertir = lambda cadena: cadena[::-1]
print(revertir("hola"))

multiplicar = lambda x,y: x*y
print(multiplicar(8,43))