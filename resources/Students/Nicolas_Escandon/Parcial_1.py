#Parcial_1
nombre = ""
entregas = 0
distancia = 0
total_km = 0
promedio = 0
respuesta = "S"

while respuesta == "S":

    nombre = input("Ingrese el nombre del conductor: ")

    entregas = int(input("Ingrese la cantidad de entregas realizadas: "))

    while entregas <= 0:
        print("Cantidad inválida. Debe ser un número positivo.")
        entregas = int(input("Ingrese la cantidad de entregas realizadas: "))

    total_km = 0
    contador = 1

    while contador <= entregas:

        distancia = float(input("Ingrese la distancia en km de la entrega: "))

        while distancia < 0:
            print("Distancia inválida. No puede ser negativa.")
            distancia = float(input("Ingrese la distancia en km de la entrega: "))

        total_km = total_km + distancia
        contador = contador + 1

    promedio = total_km / entregas

    if total_km < 50:
        categoria = "Ruta corta"
    elif total_km > 50 and total_km < 100:
        categoria = "Ruta estándar"
    else: total_km > 100
    categoria = "Ruta larga"

    print("Conductor:", nombre)
    print("Total de kilómetros recorridos:", total_km)
    print("Promedio de distancia por entrega:", promedio)
    print("Categoría de la ruta:", categoria)

    respuesta = input("¿Desea registrar otro conductor? S/N: ")
    
    

print("Programa finalizado.")










