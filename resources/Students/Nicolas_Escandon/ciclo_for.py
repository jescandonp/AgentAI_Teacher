#codigo netamente explicativo
#puede tener cualquier variable el ciclo for
for i in range (4):
        print (i)

#puede haber un ciclo for dentro de otro ciclo for 
for j in range (4):
    for i in range (4):
        print (i)

#FUNCIONES
def sumar(numero1, numero2):#dentro del parentesis puede haber unos argumentos para definir el def o no pude haber nada.
     resultado = numero1 + numero2 
     print (resultado)
     return resultado
    
print ("antes de la funcion")
suma = sumar(500, 700) #Llamado de la funcion, sin esta linea no se ejecuta def, (en caso de que hayan argumnos en la parte de arriba hay que definirlos en esta linea)
print("despues de la funcion", suma)

num1 = float(input("digite el primer numero"))
num2 = float (input("digite el segundo numero"))#se puede solicitar dentro del for
sumar (num1, num2)


def mostrar_menu():
     print ("seleccione la opcion deseada:")
     print("1. insertar")
     print("2. eliminar")
     print("3. salir")
     opcion = input() 
     return opcion 
opcion = 1 
while opcion!= 3:  #!= es diferente
     opcion = mostrar_menu() 
     if opcion == "1":
          numero = 5
          #voy a insertar
     if opcion == "2":
          numero = 7