dinero = 0
cantidad_100 = 0
cantidad_50 = 0
cantidad_20 = 0 
cantidad_10 = 0

print ("cantidad de dinero que desee retirar")
dinero = int(input())
while dinero >= 100000:
    cantidad_100 = cantidad_100 + 1
    dinero = dinero - 100000
while dinero >= 50000:
    cantidad_100 = cantidad_50 + 1
    dinero = dinero - 50000
while dinero >= 20000:
    cantidad_100 = cantidad_20 + 1
    dinero = dinero - 20000
while dinero >= 10000:
    cantidad_100 = cantidad_10 + 1
    dinero = dinero - 10000
print ("billetes de 100:", cantidad_100, "biletes de 50:", cantidad_50, "biletes de 20:", cantidad_20, "billetes de 10:", cantidad_10)

