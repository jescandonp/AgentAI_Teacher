def ingresar_sensores():
    sensores = []
    cantidad = int(input("cuantos sensores desea registrar?"))

    for i in range (cantidad):
        print(f" sensor {i + 1}")
        id_sensor = input("ID del sensor: ")
        zona =  input("zona: ")
        num_lecturas = int(input("numero de lecturas de temperatura: "))

        lecturas = []
        for j in range(num_lecturas):
            temperatura = float(input(f"temperatura {j + 1}: "))
            lecturas.append(temperatura)

        sensor = { "id": id_sensor, "zona": zona, "lecturas": lecturas}
        sensores.append(sensor)

    return sensores

def calcular_promedio(lecturas):
    return sum(lecturas) / len(lecturas)

def analizar_sensores(sensores):
    for sensor in sensores:
        promedio = calcular_promedio(sensor["lecturas"])
        sensor["promedio"] = promedio

        if promedio < 20:
            estado = "frio"
        elif promedio <= 28:
            estado = "normal"
        else:
            estado = "caliente"

        sensor["estado"] = estado

    return sensores

def mostrar_repotrte(sensores):
    for sensor in sensores:
        print(f"sensor {sensor['id']} - zona: {sensor['zona']}")
        print(f"promedio: {sensor['promedio']}")
        print(f"estado: {sensor['estado']}")

def sensor_mayor_temperatura(sensores):
    mayor = sensores[0]
    for sensor in sensores:
        if sensor["promedio"] > mayor ["promedio"]:
            mayor = sensor

    print(f"el sensor con mayor temperatura es { mayor['id']}" f"(zona: {mayor['zona']}) con un promedio de {mayor ['promedio']}")

    return mayor

sensores = ingresar_sensores()
sensores = analizar_sensores(sensores)
mostrar_repotrte(sensores)
sensor_mayor_temperatura(sensores)
