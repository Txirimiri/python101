hola = input("Bienvenidos a mi tienda. Hoy tenemos especiales de: manzanas, zumos y leche.")
print(hola)


listaDeProductos = ["manzanas", "zumos","leche","platanos","kiwis","cerezas"]
accion = int(input("Introducir '1' para ver los productos,' 2 ' para hacer una compra, y '3' para borrar un producto."))


if accion == 1:
        for producto in listaDeProductos:
    print(f"Articulo {producto}")

elif accion== 2:
    compra = input("¿Qué quieres comprar?")
    if compra in listaDeProductos:
      print(("Introduce la cantidad de dinero que tienes:?"))
      dinero=float(input())
elif accion == 3:
pass
else:
    print("No existe este opcion.")



