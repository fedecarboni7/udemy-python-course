palabra = "la casa de papel"
x = 40

diccionario = {"uno" : x, "dos" : x.__add__(10)}

print(f"{palabra.title()} tiene {diccionario['uno']} capítulos hasta la temporada 3 \ny {diccionario['dos']} hasta la temporada 4")
