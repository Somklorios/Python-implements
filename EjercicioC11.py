producto = input("¿Que producto compraste?:  ")
precio = input("¿Cual fue su precio?:  ")
precio = float(precio)
unidades_del_producto = input("¿Cuantas unidades compraste?:  ")
unidades_del_producto = int(unidades_del_producto)

total = precio * unidades_del_producto
total = str(total)

print('Es ', producto)
print('Costo ', precio)
print('Fueron ', unidades_del_producto , "Unidades")
print("El total fue de: " + total + " pesos")