class Product:
    def __init__(self, ref, nombre, precio, descripcion):
        self.ref = ref
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return f"Referencia:\t {self.ref}\n" \
               f"Nombre:\t\t {self.nombre}\n" \
               f"Precio:\t\t {self.precio}\n" \
               f"Descripcion:\t {self.descripcion}\n"


class Computacion(Product):
    marca = ""
    categoria = ""

    def __str__(self):
        return f"Referencia:\t {self.ref}\n" \
               f"Nombre:\t\t {self.nombre}\n" \
               f"Precio:\t\t {self.precio}\n" \
               f"Descripcion:\t {self.descripcion}\n" \
               f"Marca:\t\t {self.marca}\n" \
               f"Categoría:\t {self.categoria}\n"


computadora = Computacion(10010, "Dell Inspiron 15",
                          "$100.000", "Notebook Dell Inspiron i5 15,6\"")
computadora.marca = "Dell"
computadora.categoria = "Notebook"

print(computadora)
