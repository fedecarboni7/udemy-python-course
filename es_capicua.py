def pedir_numero_o_palabra():
    ingresado = input("Ingrese un número entero o una palabra: ")
    return ingresado

def es_capicua(ingresado):
    cifras = len(str(ingresado))
    posicion = 0
    capicua = True
    while(cifras > 0):
        if str(ingresado)[posicion] != str(ingresado)[cifras - 1]:
            capicua = False
        cifras -= 1
        posicion += 1
    return capicua

def main():
    if(es_capicua(pedir_numero_o_palabra())):
        print("Es capicúa")
    else:
        print("No es capicúa")
    input("\nPresionar algo para salir")

main()