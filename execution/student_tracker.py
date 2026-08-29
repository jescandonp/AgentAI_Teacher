"""
student_tracker.py - Gestor determinista del progreso de aprendizaje de los estudiantes.

Almacena el estado persistente en .tmp/student_progress.json.
Uso:
    python student_tracker.py --init
    python student_tracker.py --student python_student --get
    python student_tracker.py --student cpp_student --update-topic "Bucles" --status "Dominado" --notes "Comprende for y while"
    python student_tracker.py --summary
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Asegurar compatibilidad UTF-8 en consolas Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

DEFAULT_TOPICS = [
    "Variables y Tipos de Datos",
    "Entrada y Salida (I/O)",
    "Estructuras Condicionales",
    "Estructuras Repetitivas (Bucles)",
    "Funciones y Modularidad",
    "Arreglos y Colecciones",
    "Cadenas de Texto (Strings)",
    "Memoria y Referencias",
    "Algoritmos Fundamentales (Búsqueda/Ordenamiento)"
]

DB_PATH = Path(".tmp") / "student_progress.json"


def get_default_db() -> dict:
    return {
        "python_student": {
            "name": "Estudiante Python (Universidad A)",
            "language": "Python",
            "current_topic": "Variables y Tipos de Datos",
            "topics": {topic: {"status": "No iniciado", "notes": ""} for topic in DEFAULT_TOPICS},
            "recurring_errors": [],
            "completed_exercises": [],
            "last_updated": datetime.now().isoformat()
        },
        "cpp_student": {
            "name": "Estudiante C++ (Universidad B)",
            "language": "C++",
            "current_topic": "Variables y Tipos de Datos",
            "topics": {topic: {"status": "No iniciado", "notes": ""} for topic in DEFAULT_TOPICS},
            "recurring_errors": [],
            "completed_exercises": [],
            "last_updated": datetime.now().isoformat()
        }
    }


def load_db() -> dict:
    if not DB_PATH.exists():
        os.makedirs(DB_PATH.parent, exist_ok=True)
        db = get_default_db()
        save_db(db)
        return db
    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        db = get_default_db()
        save_db(db)
        return db


def save_db(db: dict) -> None:
    os.makedirs(DB_PATH.parent, exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)


def update_student_topic(student_id: str, topic: str, status: str, notes: str = "") -> dict:
    db = load_db()
    if student_id not in db:
        raise ValueError(f"Estudiante '{student_id}' no encontrado. Opciones: python_student, cpp_student")

    if topic not in db[student_id]["topics"]:
        db[student_id]["topics"][topic] = {}

    db[student_id]["topics"][topic]["status"] = status
    if notes:
        db[student_id]["topics"][topic]["notes"] = notes
    db[student_id]["last_updated"] = datetime.now().isoformat()
    save_db(db)
    return db[student_id]


def log_student_error(student_id: str, error_desc: str) -> dict:
    db = load_db()
    if student_id not in db:
        raise ValueError(f"Estudiante '{student_id}' no encontrado.")
    db[student_id]["recurring_errors"].append({
        "date": datetime.now().isoformat(),
        "error": error_desc
    })
    db[student_id]["last_updated"] = datetime.now().isoformat()
    save_db(db)
    return db[student_id]


def log_exercise(student_id: str, exercise_title: str, language: str, score: str = "Aprobado") -> dict:
    db = load_db()
    if student_id not in db:
        raise ValueError(f"Estudiante '{student_id}' no encontrado.")
    db[student_id]["completed_exercises"].append({
        "date": datetime.now().isoformat(),
        "title": exercise_title,
        "language": language,
        "score": score
    })
    db[student_id]["last_updated"] = datetime.now().isoformat()
    save_db(db)
    return db[student_id]


def generate_summary() -> str:
    db = load_db()
    lines = ["# 📊 Resumen de Progreso de Estudiantes\n"]

    for sid, data in db.items():
        lines.append(f"## 👤 {data['name']} ({data['language']})")
        lines.append(f"- **Tema actual:** {data.get('current_topic', 'N/A')}")
        lines.append(f"- **Ejercicios completados:** {len(data.get('completed_exercises', []))}")
        lines.append(f"- **Errores registrados:** {len(data.get('recurring_errors', []))}")
        lines.append("\n### Estado de Temas:")
        lines.append("| Tema | Estado | Notas |")
        lines.append("| :--- | :--- | :--- |")
        for topic, tdata in data.get("topics", {}).items():
            status_icon = "⚪"
            if tdata.get("status") == "Dominado":
                status_icon = "🟢"
            elif tdata.get("status") == "En progreso":
                status_icon = "🟡"
            elif tdata.get("status") == "Con dificultades":
                status_icon = "🔴"
            lines.append(f"| {topic} | {status_icon} {tdata.get('status', 'No iniciado')} | {tdata.get('notes', '')} |")
        lines.append("\n---\n")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Gestor de progreso de estudiantes.")
    parser.add_argument("--init", action="store_true", help="Inicializar la base de datos de progreso")
    parser.add_argument("--student", choices=["python_student", "cpp_student"], help="ID del estudiante")
    parser.add_argument("--get", action="store_true", help="Obtener estado del estudiante")
    parser.add_argument("--update-topic", type=str, help="Nombre del tema a actualizar")
    parser.add_argument("--status", choices=["No iniciado", "En progreso", "Dominado", "Con dificultades"], help="Nuevo estado del tema")
    parser.add_argument("--notes", type=str, default="", help="Notas adicionales sobre el tema")
    parser.add_argument("--log-error", type=str, help="Registrar un error común del estudiante")
    parser.add_argument("--log-exercise", type=str, help="Registrar un ejercicio completado")
    parser.add_argument("--summary", action="store_true", help="Imprimir resumen general en Markdown")

    args = parser.parse_args()

    if args.init:
        db = get_default_db()
        save_db(db)
        print(json.dumps({"message": "Base de datos inicializada con éxito", "db_path": str(DB_PATH)}, indent=2))
        return

    if args.summary:
        print(generate_summary())
        return

    if args.student:
        if args.get:
            db = load_db()
            print(json.dumps(db[args.student], indent=2, ensure_ascii=False))
        elif args.update_topic and args.status:
            res = update_student_topic(args.student, args.update_topic, args.status, args.notes)
            print(json.dumps({"message": f"Tema '{args.update_topic}' actualizado", "student": res}, indent=2, ensure_ascii=False))
        elif args.log_error:
            res = log_student_error(args.student, args.log_error)
            print(json.dumps({"message": "Error registrado", "student": res}, indent=2, ensure_ascii=False))
        elif args.log_exercise:
            lang = "Python" if args.student == "python_student" else "C++"
            res = log_exercise(args.student, args.log_exercise, lang)
            print(json.dumps({"message": "Ejercicio registrado", "student": res}, indent=2, ensure_ascii=False))
    else:
        # Por defecto si no hay argumentos, mostrar el resumen
        print(generate_summary())


if __name__ == "__main__":
    main()
