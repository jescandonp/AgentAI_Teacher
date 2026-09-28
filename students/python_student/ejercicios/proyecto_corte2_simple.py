"""
proyecto_corte2_simple.py
Sistema de Gestión y Análisis de Rendimiento de Jugadores de Fútbol.
Nivel: Fundamentos de Programación (Corte 2).
"""

import json
import os
from typing import Any, Dict, List, Optional, Tuple

# Ruta absoluta al archivo JSON vinculada dinámicamente al directorio del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "jugadores.json")


# ==========================================
# FUNCIONES DE ENTRADA Y VALIDACIÓN (E)
# ==========================================

def pedir_numero_mayor_a_cero(mensaje: str) -> int:
    """Solicita al usuario un número entero estrictamente mayor a 0."""
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        print("Eso no es un número válido, debe ser mayor a 0. Intenta de nuevo.")


def pedir_numero_cero_o_mas(mensaje: str) -> int:
    """Solicita al usuario un número entero mayor o igual a 0."""
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit():
            return int(dato)
        print("Eso no es un número válido. Intenta de nuevo.")


def pedir_texto(mensaje: str) -> str:
    """Solicita una cadena de texto asegurando que no quede vacía."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Este dato no puede quedar vacío.")


# ==========================================
# PERSISTENCIA DE DATOS (JSON)
# ==========================================

def cargar_jugadores() -> List[Dict[str, Any]]:
    """Carga la lista de jugadores desde el archivo JSON."""
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Aviso: El archivo estaba dañado o vacío, se iniciará una lista nueva.")
        return []


def guardar_jugadores(lista_jugadores: List[Dict[str, Any]]) -> bool:
    """Guarda la lista completa de jugadores en el archivo JSON."""
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(lista_jugadores, f, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print("Error: No se pudo guardar el archivo:", error)
        return False


# ==========================================
# FUNCIONES DE PROCESAMIENTO Y ANÁLISIS (P)
# ==========================================

def calcular_totales_y_promedios(goles: List[int], asistencias: List[int]) -> Tuple[int, int, float, float]:
    """Calcula la suma total y los promedios por partido de goles y asistencias."""
    partidos = len(goles)
    if partidos == 0:
        return 0, 0, 0.0, 0.0

    total_goles = sum(goles)
    total_asistencias = sum(asistencias)
    promedio_goles = total_goles / partidos
    promedio_asistencias = total_asistencias / partidos

    return total_goles, total_asistencias, promedio_goles, promedio_asistencias


def encontrar_mejor_partido(goles: List[int], asistencias: List[int]) -> Optional[Dict[str, Any]]:
    """Identifica el partido con mayor aporte ofensivo combinado (goles + asistencias)."""
    if len(goles) == 0:
        return None

    mejor_partido = 0
    mejor_aporte = goles[0] + asistencias[0]

    for i in range(len(goles)):
        aporte = goles[i] + asistencias[i]
        if aporte > mejor_aporte:
            mejor_aporte = aporte
            mejor_partido = i

    return {
        "numero_partido": mejor_partido + 1,
        "goles": goles[mejor_partido],
        "asistencias": asistencias[mejor_partido],
        "aportes": mejor_aporte
    }


def definir_categoria(promedio_goles: float, promedio_asistencias: float) -> str:
    """Clasifica el perfil del jugador según su rendimiento promedio por partido."""
    if promedio_goles >= 1.5:
        return "Goleador Destacado"
    if promedio_asistencias >= 1.0:
        return "Creador de Juego"
    if (promedio_goles + promedio_asistencias) >= 1.5:
        return "Jugador Equilibrado"
    return "Jugador en Desarrollo"


def crear_plan_entrenamiento(promedio_goles: float, promedio_asistencias: float, categoria: str) -> Dict[str, Any]:
    """Genera un plan de entrenamiento adaptativo según el diagnóstico del jugador."""
    if promedio_goles < 0.5 and promedio_asistencias < 0.5:
        objetivo = "Participar más en el juego ofensivo y tocar más el balón."
        rutina = [
            "Control y conducción de balón: 3 veces por semana, 25 minutos.",
            "Pase corto y definición básica: 30 repeticiones por pierna.",
            "Practicar desmarques para ofrecer opciones de pase en ataque."
        ]
    elif promedio_goles < 1.0:
        objetivo = "Mejorar la puntería y efectividad frente al arco."
        rutina = [
            "Remates de primera dentro del área: 40 repeticiones por sesión.",
            "Tiro con ambas piernas y mano a mano contra el portero.",
            "Seguir practicando pases para no perder nivel en asistencias."
        ]
    elif promedio_asistencias < 0.75:
        objetivo = "Mejorar la visión de juego y el último pase."
        rutina = [
            "Pases largos y cambios de frente: 30 balones con precisión.",
            "Acostumbrarse a mirar el campo antes de recibir el balón.",
            "Centros al área con un defensor marcando de cerca."
        ]
    else:
        objetivo = "Mantener el buen nivel y mejorar la toma de decisiones."
        rutina = [
            "Definición bajo presión en espacios reducidos.",
            "Transiciones rápidas de defensa a ataque.",
            "Simular jugadas reales tomando decisiones en 2 toques."
        ]

    return {
        "categoria": categoria,
        "objetivo": objetivo,
        "rutina": rutina
    }


def buscar_jugador(jugadores: List[Dict[str, Any]], criterio: str) -> Optional[Dict[str, Any]]:
    """
    Busca un jugador por documento exacto o por coincidencia parcial en el nombre.
    Prioriza la búsqueda por documento exacto para evitar ambigüedades.
    """
    criterio_limpio = criterio.strip().lower()

    # 1. Búsqueda prioritaria por documento exacto
    for j in jugadores:
        if j["documento"].strip().lower() == criterio_limpio:
            return j

    # 2. Búsqueda por subcadena en el nombre
    for j in jugadores:
        if criterio_limpio in j["nombre"].lower():
            return j

    return None


# ==========================================
# ACCIONES DEL MENÚ Y VISTAS (S)
# ==========================================

def registrar_jugador() -> None:
    """Gestiona el flujo completo de registro de un nuevo jugador."""
    print("\n=== REGISTRAR NUEVO JUGADOR ===")

    jugadores = cargar_jugadores()
    documento = pedir_texto("Documento del jugador: ")

    for j in jugadores:
        if j["documento"] == documento:
            print(f"Aviso: Ya hay un jugador con ese documento ({j['nombre']}).")
            return

    nombre = pedir_texto("Nombre completo: ")
    cantidad_partidos = pedir_numero_mayor_a_cero("¿Cuántos partidos jugó?: ")

    goles: List[int] = []
    asistencias: List[int] = []

    print("\nRegistro partido a partido:")
    for i in range(cantidad_partidos):
        print(f"\nPartido {i + 1}:")
        g = pedir_numero_cero_o_mas("  Goles: ")
        a = pedir_numero_cero_o_mas("  Asistencias: ")
        goles.append(g)
        asistencias.append(a)

    total_goles, total_asistencias, prom_goles, prom_asistencias = calcular_totales_y_promedios(goles, asistencias)
    mejor_partido = encontrar_mejor_partido(goles, asistencias)
    categoria = definir_categoria(prom_goles, prom_asistencias)
    plan = crear_plan_entrenamiento(prom_goles, prom_asistencias, categoria)

    nuevo_jugador: Dict[str, Any] = {
        "documento": documento,
        "nombre": nombre,
        "cantidad_partidos": cantidad_partidos,
        "goles": goles,
        "asistencias": asistencias,
        "estadisticas": {
            "total_goles": total_goles,
            "total_asistencias": total_asistencias,
            "promedio_goles": round(prom_goles, 2),
            "promedio_asistencias": round(prom_asistencias, 2),
            "mejor_partido": mejor_partido,
            "categoria": categoria
        },
        "plan_entrenamiento": plan
    }

    jugadores.append(nuevo_jugador)

    if guardar_jugadores(jugadores):
        print("\n¡Listo! Jugador guardado con éxito.")
        print("Categoría asignada:", categoria)
        print(f"Total goles: {total_goles} | Total asistencias: {total_asistencias}")
        print(f"Promedio goles: {round(prom_goles, 2)} | Promedio asistencias: {round(prom_asistencias, 2)}")


def ver_ficha_jugador() -> None:
    """Muestra en pantalla el resumen detallado y rendimiento por partido de un jugador."""
    print("\n=== CONSULTAR FICHA DE JUGADOR ===")

    jugadores = cargar_jugadores()
    if not jugadores:
        print("Todavía no hay jugadores registrados.")
        return

    criterio = pedir_texto("Documento o nombre a buscar: ")
    jugador = buscar_jugador(jugadores, criterio)

    if jugador is None:
        print("No se encontró ningún jugador con ese dato.")
        return

    stats = jugador["estadisticas"]
    mejor = stats["mejor_partido"]

    print("\n----------------------------------------")
    print(f"FICHA DE: {jugador['nombre'].upper()}")
    print("----------------------------------------")
    print("Documento:            ", jugador["documento"])
    print("Partidos jugados:     ", jugador["cantidad_partidos"])
    print("Total goles:          ", stats["total_goles"])
    print("Total asistencias:    ", stats["total_asistencias"])
    print("Promedio de goles:    ", stats["promedio_goles"])
    print("Promedio asistencias: ", stats["promedio_asistencias"])
    print("Categoría:            ", stats["categoria"])

    if mejor is not None:
        print(f"Mejor partido:         Partido #{mejor['numero_partido']} ({mejor['aportes']} aportes directos)")

    print("\nDetalle por partido:")
    for i in range(len(jugador["goles"])):
        g = jugador["goles"][i]
        a = jugador["asistencias"][i]
        print(f"  Partido {i + 1:02d}: {g} gol(es), {a} asistencia(s)")


def ver_plan_entrenamiento() -> None:
    """Muestra el plan pedagógico y de entrenamiento asignado a un jugador."""
    print("\n=== PLAN DE ENTRENAMIENTO ===")

    jugadores = cargar_jugadores()
    if not jugadores:
        print("Todavía no hay jugadores registrados.")
        return

    criterio = pedir_texto("Documento o nombre del jugador: ")
    jugador = buscar_jugador(jugadores, criterio)

    if jugador is None:
        print("No se encontró ningún jugador con ese dato.")
        return

    stats = jugador["estadisticas"]
    plan = jugador.get("plan_entrenamiento")

    # Si por compatibilidad con datos antiguos no existe el plan, se genera dinámicamente
    if not plan:
        plan = crear_plan_entrenamiento(stats["promedio_goles"], stats["promedio_asistencias"], stats["categoria"])

    print(f"\nPlan para: {jugador['nombre'].upper()} ({stats['categoria']})")
    print("Objetivo: ", plan["objetivo"])
    print("\nRutina sugerida:")
    for i, paso in enumerate(plan["rutina"], 1):
        print(f"  {i}. {paso}")


def listar_jugadores() -> None:
    """Lista un resumen tabular simple de todos los jugadores registrados."""
    print("\n=== LISTA DE JUGADORES ===")

    jugadores = cargar_jugadores()
    if not jugadores:
        print("Todavía no hay jugadores registrados.")
        return

    for j in jugadores:
        stats = j["estadisticas"]
        print(f"- {j['nombre']} (Doc: {j['documento']}) | "
              f"Partidos: {j['cantidad_partidos']} | "
              f"Goles: {stats['total_goles']} | "
              f"Asistencias: {stats['total_asistencias']} | "
              f"Categoría: {stats['categoria']}")

    print(f"\nTotal de jugadores registrados: {len(jugadores)}")


def eliminar_jugador() -> None:
    """Elimina un jugador tras confirmación explícita por documento."""
    print("\n=== ELIMINAR JUGADOR ===")

    jugadores = cargar_jugadores()
    if not jugadores:
        print("Todavía no hay jugadores registrados.")
        return

    documento = pedir_texto("Documento del jugador a eliminar: ")

    jugador_encontrado: Optional[Dict[str, Any]] = None
    for j in jugadores:
        if j["documento"] == documento:
            jugador_encontrado = j
            break

    if jugador_encontrado is None:
        print("No se encontró ningún jugador con ese documento.")
        return

    confirmacion = input(f"¿Seguro que deseas eliminar a '{jugador_encontrado['nombre']}'? (s/n): ").strip().lower()

    if confirmacion == "s":
        jugadores.remove(jugador_encontrado)
        if guardar_jugadores(jugadores):
            print("Jugador eliminado con éxito.")
    else:
        print("Operación cancelada. El jugador no fue eliminado.")


# ==========================================
# MENÚ PRINCIPAL Y CONTROLADOR
# ==========================================

def mostrar_menu() -> None:
    """Imprime el menú de opciones del sistema."""
    print("\n=========================")
    print("   SISTEMA DE JUGADORES  ")
    print("=========================")
    print("1. Registrar jugador")
    print("2. Ver ficha de un jugador")
    print("3. Ver plan de entrenamiento")
    print("4. Listar todos los jugadores")
    print("5. Eliminar jugador")
    print("6. Salir")


def main() -> None:
    """Función principal que orquesta el ciclo de vida de la aplicación."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "1":
            registrar_jugador()
        elif opcion == "2":
            ver_ficha_jugador()
        elif opcion == "3":
            ver_plan_entrenamiento()
        elif opcion == "4":
            listar_jugadores()
        elif opcion == "5":
            eliminar_jugador()
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor ingresa un número del 1 al 6.")


if __name__ == "__main__":
    main()


