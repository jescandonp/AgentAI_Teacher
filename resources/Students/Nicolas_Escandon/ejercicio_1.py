#este programa calcula el promedio de tres notas
print ("Por favor ingrese la primera calificacion")
calificacion_1 = float(input("Por favor ingrese la primera calificacion")) 

print ("Por favor ingrese la segunda calificacion")
calificacion_2 = float(input()) 

print ("Por favor ingrese la tercera calificacion")
calificacion_3 = float(input()) 

promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3 

if promedio >= 60:
    estado = "aprobado"
else:
    estado = "reprobado"

print ("----------------------------------")
print ("el promedio del estudiante es:", promedio) 
print ("el estado del estudiante es:", estado) 

