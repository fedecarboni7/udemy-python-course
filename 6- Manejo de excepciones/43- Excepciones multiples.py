#Obtener el tipo de error
try:
    num = int(input("Ingrese un numero distinto a 0: "))
    print(f"100 / {num} = {100/num}")
except Exception as e:
    print("Ocurrió el siguente error: ", type(e).__name__)

#Crear excepciones para cada tipo de error
try:
    num = int(input("Ingrese un numero distinto a 0: "))
    print(f"100 / {num} = {100/num}")
except ValueError:
    print("Tiene que ingresarse un numero entero")
except ZeroDivisionError:
    print("El numero tiene que ser distinto a 0")