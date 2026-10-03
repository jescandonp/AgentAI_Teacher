"""
run_refuerzo_cpp.py - Corrector determinista de las tareas de refuerzo en C++ (Juan Diego).

Compila cada entrega, la ejecuta con los casos de prueba del PDF
"Tareas-Refuerzo-CPP-Juan-Diego" y reporta aprobado/fallado por caso.

Las verificaciones son INDICATIVAS (buscan los valores esperados en la salida, sin
depender del texto exacto de los mensajes). El tutor sigue leyendo la salida y el codigo.

Uso:
    python run_refuerzo_cpp.py --dir ruta/con/entregas
    python run_refuerzo_cpp.py --dir ruta --ej 3 --verbose
    python run_refuerzo_cpp.py --dir ruta --json

Archivos esperados en --dir: ej1_sensores.cpp, ej2_notas.cpp, ej3_facturacion.cpp
Requiere g++, clang++ o cl en el PATH.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

TIMEOUT_S = 3
MAX_OUT_BYTES = 200_000

ARCHIVOS = {1: "ej1_sensores.cpp", 2: "ej2_notas.cpp", 3: "ej3_facturacion.cpp"}

NOTAS_BASE = ["3.5", "4.2", "2.8", "5.0", "3.0", "4.8", "1.5", "3.5", "4.0", "2.7"]

# Cada caso: nombre, tokens de entrada (se envian uno por linea) y verificaciones.
#   ("num", valor)   -> el numero aparece en la salida (tolera 13.537,5 / 13537.5 / 13537.50)
#   ("re", patron)   -> el patron (sin distinguir mayusculas) aparece en la salida
CASOS = {
    1: [
        {"nombre": "Principal: promedio 25.25, 3 criticas, 2 bajas",
         "entrada": ["36.5", "12.0", "20.0", "35.0", "14.9", "28.5", "40.1", "15.0"],
         "checks": [("num", 25.25),
                    ("re", r"(cr.tic\w*[^\n\d]*\b3\b|\b3\b[^\n\d]*cr.tic)"),
                    ("re", r"(baj\w*[^\n\d]*\b2\b|\b2\b[^\n\d]*baj)")]},
        {"nombre": "Bordes: 35.0 es critica, 15.0 NO es baja (1 critica, 0 bajas)",
         "entrada": ["35.0", "15.0", "20", "20", "20", "20", "20", "20"],
         "checks": [("re", r"(cr.tic\w*[^\n\d]*\b1\b|\b1\b[^\n\d]*cr.tic)"),
                    ("re", r"(baj\w*[^\n\d]*\b0\b|\b0\b[^\n\d]*baj)")]},
    ],
    2: [
        {"nombre": "Principal + buscar 3.5: promedio 3.50, mejor 5.0, indice 0",
         "entrada": NOTAS_BASE + ["3.5"],
         "checks": [("num", 3.5), ("num", 5.0), ("re", r"\b0\b")]},
        {"nombre": "Buscar 4.5: no esta (-1)",
         "entrada": NOTAS_BASE + ["4.5"],
         "checks": [("re", r"(no (est|se encuentr|existe|fue|hay)|-1)")]},
        {"nombre": "Validacion: rechaza 5.5 y -1 (el promedio sigue en 3.50)",
         "entrada": ["5.5", "-1"] + NOTAS_BASE + ["3.5"],
         "checks": [("num", 3.5), ("re", r"(inv.lid|rango|entre|0\.0|vuelva|nuevo|error)")]},
    ],
    3: [
        {"nombre": "Carrito 102x2 + 105x3: 165.000 / 16.500 / 28.215 / 176.715",
         "entrada": ["2", "102", "2", "2", "105", "3", "4", "5"],
         "checks": [("num", 165000), ("num", 16500), ("num", 28215), ("num", 176715),
                    ("re", r"105")]},
        {"nombre": "Borde 150.000: 5% (7.500 / 27.075 / 169.575)",
         "entrada": ["2", "103", "1", "2", "102", "1", "2", "105", "1", "4", "5"],
         "checks": [("num", 150000), ("num", 7500), ("num", 27075), ("num", 169575)]},
        {"nombre": "101x5: 75.000 / 3.750 / 13.537,5 / 84.787,5",
         "entrada": ["2", "101", "5", "4", "5"],
         "checks": [("num", 75000), ("num", 3750), ("num", 13537.5), ("num", 84787.5)]},
        {"nombre": "Sin descuento: 105x2 + 101x1: 65.000 / 12.350 / 77.350",
         "entrada": ["2", "105", "2", "2", "101", "1", "4", "5"],
         "checks": [("num", 65000), ("num", 12350), ("num", 77350)]},
        {"nombre": "Stock: agregar 104x4 se rechaza (solo hay 3)",
         "entrada": ["2", "104", "4", "5"],
         "checks": [("re", r"(solo hay|stock|insuficiente|no hay|disponible)")]},
        {"nombre": "Codigo inexistente 999",
         "entrada": ["2", "999", "1", "5"],
         "checks": [("re", r"(no existe|inv.lid|no encontr|no se encontr)")]},
        {"nombre": "Inventario: tras 102x2 y 105x3, el catalogo muestra stock 6 y 9",
         "entrada": ["2", "102", "2", "2", "105", "3", "1", "5"],
         "checks": [("num", 6), ("num", 9)]},
    ],
}


# ---------------------------------------------------------------- verificacion pura
def numeros_en_texto(texto: str) -> list:
    """Extrae todos los numeros de la salida, tolerando separadores de miles y comas."""
    encontrados = []
    for crudo in re.findall(r"-?\d[\d.,]*", texto):
        crudo = crudo.rstrip(".,")
        candidatos = {crudo}
        if re.fullmatch(r"-?\d{1,3}(\.\d{3})+", crudo):        # 165.000 -> 165000
            candidatos.add(crudo.replace(".", ""))
        if re.fullmatch(r"-?\d{1,3}(\.\d{3})+,\d+", crudo):    # 13.537,5 -> 13537.5
            candidatos.add(crudo.replace(".", "").replace(",", "."))
        if re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", crudo):  # 13,537.5 -> 13537.5
            candidatos.add(crudo.replace(",", ""))
        if re.fullmatch(r"-?\d+,\d+", crudo):                  # 3,5 -> 3.5
            candidatos.add(crudo.replace(",", "."))
        for c in candidatos:
            try:
                encontrados.append(float(c))
            except ValueError:
                pass
    return encontrados


def evaluar(checks: list, salida: str) -> list:
    """Devuelve la lista de verificaciones que fallaron (vacia = caso aprobado)."""
    fallos = []
    nums = None
    for tipo, valor in checks:
        if tipo == "num":
            if nums is None:
                nums = numeros_en_texto(salida)
            if not any(abs(n - valor) < 0.01 for n in nums):
                fallos.append(f"no aparece el numero {valor:g}")
        elif tipo == "re":
            if not re.search(valor, salida, re.IGNORECASE):
                fallos.append(f"no aparece el patron /{valor}/")
    return fallos


def revisar_estatico(codigo: str) -> list:
    """Alertas de estilo/limites sobre el codigo fuente."""
    alertas = []
    for n, linea in enumerate(codigo.splitlines(), 1):
        if re.search(r"for\s*\([^;]*;\s*\w+\s*<=\s*(TAM|MAX_PROD|MAX|\w*[Tt]am\w*|\d+)\s*;", linea):
            alertas.append(f"L{n}: bucle con '<=' contra el tamano (posible desbordamiento): {linea.strip()}")
        if re.search(r"\b(double|float|int)\s+(suma|total|subtotal|contador|cont\w*)\s*;", linea):
            alertas.append(f"L{n}: acumulador/contador sin inicializar: {linea.strip()}")
    return alertas


# ---------------------------------------------------------------- compilacion y ejecucion
def detectar_compilador():
    for nombre in ("g++", "clang++", "cl"):
        ruta = shutil.which(nombre)
        if ruta:
            return nombre, ruta
    return None, None


def compilar(fuente: str, salida_exe: str, compilador: tuple):
    nombre, ruta = compilador
    if nombre == "cl":
        cmd = [ruta, "/nologo", "/EHsc", "/W3", f"/Fe:{salida_exe}", f"/Fo:{salida_exe}.obj", fuente]
    else:
        cmd = [ruta, "-std=c++17", "-Wall", "-Wextra", fuente, "-o", salida_exe]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode == 0, (p.stdout + p.stderr).strip()


def ejecutar(exe: str, entrada: list):
    """Ejecuta con stdin finito; la salida va a un archivo para no saturar memoria en bucles infinitos."""
    with tempfile.TemporaryFile() as out:
        try:
            proc = subprocess.run([exe], input="\n".join(entrada) + "\n", text=True, encoding="utf-8",
                                  errors="replace", stdout=out, stderr=subprocess.STDOUT, timeout=TIMEOUT_S)
            timeout = False
            codigo = proc.returncode
        except subprocess.TimeoutExpired:
            timeout, codigo = True, None
        out.seek(0)
        texto = out.read(MAX_OUT_BYTES).decode("utf-8", errors="replace")
    return texto, codigo, timeout


def revisar_ejercicio(num: int, directorio: str, compilador, verbose: bool) -> dict:
    ruta = os.path.join(directorio, ARCHIVOS[num])
    res = {"ejercicio": num, "archivo": ARCHIVOS[num], "estado": "", "alertas": [], "casos": []}
    if not os.path.isfile(ruta):
        res["estado"] = "NO ENTREGADO"
        return res

    with open(ruta, encoding="utf-8", errors="replace") as f:
        res["alertas"] = revisar_estatico(f.read())

    with tempfile.TemporaryDirectory() as tmp:
        exe = os.path.join(tmp, "entrega.exe" if os.name == "nt" else "entrega")
        ok, log = compilar(ruta, exe, compilador)
        res["compilacion"] = log
        if not ok:
            res["estado"] = "NO COMPILA"
            return res
        for caso in CASOS[num]:
            salida, codigo, timeout = ejecutar(exe, caso["entrada"])
            fallos = evaluar(caso["checks"], salida)
            if timeout:
                fallos.insert(0, f"TIMEOUT ({TIMEOUT_S}s): posible bucle infinito o espera de mas datos")
            elif codigo not in (0, None):
                fallos.insert(0, f"termino con codigo {codigo} (posible fallo en ejecucion)")
            res["casos"].append({"nombre": caso["nombre"], "aprobado": not fallos, "fallos": fallos,
                                 "salida": salida if (verbose or fallos) else ""})
    pasados = sum(c["aprobado"] for c in res["casos"])
    res["estado"] = f"{pasados}/{len(res['casos'])} casos"
    res["aprobado"] = pasados == len(res["casos"])
    return res


def imprimir(resultados: list, verbose: bool):
    for r in resultados:
        print(f"\n=== Ejercicio {r['ejercicio']} ({r['archivo']}): {r['estado']} ===")
        for a in r["alertas"]:
            print(f"  [ALERTA] {a}")
        if r["estado"] == "NO COMPILA":
            print(r.get("compilacion", ""))
            continue
        for c in r["casos"]:
            print(f"  [{'OK' if c['aprobado'] else 'FALLA'}] {c['nombre']}")
            for f in c["fallos"]:
                print(f"        - {f}")
            if c["salida"] and (verbose or not c["aprobado"]):
                for linea in c["salida"].splitlines()[:25]:
                    print(f"        | {linea}")
        if r.get("compilacion"):
            print("  [Advertencias del compilador]")
            for linea in r["compilacion"].splitlines()[:15]:
                print(f"        {linea}")


def main():
    ap = argparse.ArgumentParser(description="Corrector de las tareas de refuerzo C++ de Juan Diego")
    ap.add_argument("--dir", required=True, help="Carpeta con ej1_sensores.cpp, ej2_notas.cpp, ej3_facturacion.cpp")
    ap.add_argument("--ej", default="all", choices=["1", "2", "3", "all"])
    ap.add_argument("--verbose", action="store_true", help="Muestra la salida de todos los casos")
    ap.add_argument("--json", action="store_true", help="Salida en JSON")
    args = ap.parse_args()

    compilador = detectar_compilador()
    if compilador[0] is None:
        print("ERROR: no se encontro g++, clang++ ni cl en el PATH. Instala un compilador de C++ "
              "(por ejemplo MinGW-w64 o MSYS2) y vuelve a ejecutar.", file=sys.stderr)
        return 2

    numeros = [1, 2, 3] if args.ej == "all" else [int(args.ej)]
    resultados = [revisar_ejercicio(n, args.dir, compilador, args.verbose) for n in numeros]

    if args.json:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
    else:
        print(f"Compilador: {compilador[0]}")
        imprimir(resultados, args.verbose)
    todo_ok = all(r.get("aprobado") for r in resultados)
    return 0 if todo_ok else 1


if __name__ == "__main__":
    sys.exit(main())
