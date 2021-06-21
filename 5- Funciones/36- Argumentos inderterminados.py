def argumentar(*argumentos):
    print(argumentos)

print("argumentar")
argumentar(5, "Hola", {2: "dos", 3: "tres"})

def nombrar(**keywordargs):
    print(keywordargs)

print("\nnombrar")
nombrar(num = 5, nombre = "Fede", lista = [0, 1, 2])

def nombrar_kw(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
        
print("\nnombrar_kw")
nombrar_kw(num = 5, nombre = "Fede", lista = [0, 1, 2])

def nombrar_todo(**cosas):
    for clave in cosas:
        print(clave, ": ", cosas[clave], sep='')

print("\nnombrar_todo")
nombrar_todo(num = 5, nombre = "Fede", lista = [0, 1, 2])

def super_nominacion(*args, **kwargs):
    suma = 0
    for e in args:
        suma += e
    print(f"El promedio es {suma/len(args)}")
    for clave in kwargs:
        print(clave, "\t", kwargs[clave])

print("\nsuper_nominacion")
super_nominacion(8, 7, 9, 6, padron = 106911, nombre = "Fede", edad = 21, notas = [8, 7, 9, 6])