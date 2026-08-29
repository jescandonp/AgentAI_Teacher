notas = []

def ingresar_calificaciones():
    cantidad_de_calificaciones = int(input("Cantidad de notas que desee ingresar:"))
    for i in range (cantidad_de_calificaciones):
        calificaciones = float(input("Ingrese la calificacion:"))
        notas.append(calificaciones)
    return notas
notas = ingresar_calificaciones()



def mostras_calificaciones():
    for i in range (len(notas)):
        print (notas[i])
print("Las calificaciones ingresadas fueron:")  
mostras_calificaciones()

def calclular_promedio():
    promedio = sum (notas) / len(notas)
    print ("El promedio de calificaciones", promedio)
    if notas == 0:
        return 0.0
calclular_promedio()

def obtener_extremos():
    maximo = max (notas)
    minimo = min (notas)
    return notas
obtener_extremos()



def mostrar_menu():
    
    print ("1. Calcular promedio")
    print ("2. Calificacion mas alta")
    print ("3. Calificacion mas baja")
    return "opcion"

repetir = "si"

while repetir == "si":
    mostrar_menu()
    opcion = int(input("Seleccione una opcion:"))
    if opcion == 1:
        calclular_promedio()
    elif opcion == 2:
        print(max(notas))
    else:
        print(min(notas))
    repetir == "si"
    repetir = str(input("Desea seleccionar otra opcion? (si/no):"))
print ("Hasta la proxima")

    
    