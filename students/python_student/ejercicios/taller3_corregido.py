"""
Taller 3 - Gestión de Calificaciones (Versión Refactorizada)
Estudiante: Nicolás Escandón
Universidad: Universidad EAN
Curso: Algoritmos y Programación - Fundamentos
"""

# -------------------------------------------------------------
# 1. ZONA DE DEFINICIÓN DE FUNCIONES (Caja de Herramientas)
# -------------------------------------------------------------

def ingresar_calificaciones():
    """Solicita y valida la cantidad de notas a ingresar."""
    notas_nuevas = []
    cantidad = int(input("¿Cuántas notas desea ingresar?: "))
    
    while cantidad <= 0:
        print("La cantidad de notas debe ser al menos 1.")
        cantidad = int(input("Ingrese una cantidad válida: "))
        
    for i in range(cantidad):
        nota = float(input(f"Ingrese la calificación #{i + 1}: "))
        while nota < 0 or nota > 100:
            print("Calificación inválida. Debe estar entre 0 y 100.")
            nota = float(input(f"Ingrese nuevamente la calificación #{i + 1}: "))
        notas_nuevas.append(nota)
        
    return notas_nuevas


def mostrar_calificaciones(notas):
    """Muestra el listado de calificaciones almacenadas."""
    if len(notas) == 0:
        print("⚠️ No hay notas registradas.")
    else:
        print("\n📋 Calificaciones ingresadas:")
        for i in range(len(notas)):
            print(f"  Nota #{i + 1}: {notas[i]}")


def calcular_promedio(notas):
    """Calcula el promedio asegurando que la lista no esté vacía."""
    if len(notas) == 0:
        print("⚠️ No hay calificaciones para calcular el promedio.")
        return 0.0
    
    promedio = sum(notas) / len(notas)
    print(f"📊 El promedio de calificaciones es: {promedio:.2f}")
    return promedio


def obtener_extremos(notas):
    """Devuelve una tupla con (nota_maxima, nota_minima)."""
    if len(notas) == 0:
        print("⚠️ No hay calificaciones registradas.")
        return None, None
    
    maximo = max(notas)
    minimo = min(notas)
    return maximo, minimo


def mostrar_menu():
    """Imprime el menú de opciones y retorna la opción seleccionada."""
    print("\n" + "=" * 35)
    print("      MENÚ DE CALIFICACIONES")
    print("=" * 35)
    print("1. Calcular promedio")
    print("2. Calificación más alta")
    print("3. Calificación más baja")
    print("4. Ver todas las calificaciones")
    print("5. Salir")
    print("=" * 35)
    opcion = int(input("Seleccione una opción (1-5): "))
    return opcion


# -------------------------------------------------------------
# 2. ZONA DE FLUJO PRINCIPAL (Modelo E-P-S)
# -------------------------------------------------------------

def main():
    print("=== SISTEMA DE CALIFICACIONES - UNIVERSIDAD EAN ===")
    
    # ENTRADA: Captura inicial de datos
    calificaciones = ingresar_calificaciones()
    
    repetir = "si"
    while repetir.lower() == "si":
        opcion = mostrar_menu()
        
        # PROCESOS Y SALIDAS SEGÚN LA OPCIÓN
        if opcion == 1:
            calcular_promedio(calificaciones)
            
        elif opcion == 2:
            maxima, minima = obtener_extremos(calificaciones)
            if maxima is not None:
                print(f"⭐ La calificación más alta es: {maxima}")
                
        elif opcion == 3:
            maxima, minima = obtener_extremos(calificaciones)
            if minima is not None:
                print(f"🔻 La calificación más baja es: {minima}")
                
        elif opcion == 4:
            mostrar_calificaciones(calificaciones)
            
        elif opcion == 5:
            print("Saliendo del menú...")
            break
            
        else:
            print("❌ Opción inválida. Por favor elija un número del 1 al 5.")
            
        repetir = input("\n¿Desea seleccionar otra opción? (si/no): ")
        
    print("\nPrograma finalizado. ¡Hasta la próxima!")


if __name__ == "__main__":
    main()
