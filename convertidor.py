def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tiene?: ")
    pesos = float (pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $  " + dolares + "  dolares")



menu = """
Bienvenido al conversor de monedas $

1 - Pesos Colombianos
2 - Pesos argentina
3 - Pesos mexicanos


Elige una opcion:  """

opcion = int(input(menu))


if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 150)
elif opcion == 3:
    conversor("Mexicanos", 20.14)
else:
    print("Ingresa una opcion correcta por favor")






