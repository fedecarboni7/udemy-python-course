#Uso de try, except, else, y finally.

try:
    num = int(input("Ingrese un número entero: "))
    print("La mitad del número es:", num/2)
except:
    print("Intente de nuevo.")
else:
    print("Ejecución exitosa")
finally:
    print("Termina un ciclo")
