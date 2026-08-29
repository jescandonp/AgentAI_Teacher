"""
generate_trace_table.py - Generador determinista de plantillas de trazas de ejecución y diagramas Mermaid.

Uso:
    python generate_trace_table.py --type trace --vars "i,total,n" --steps 4
    python generate_trace_table.py --type flowchart --template while_loop
"""

import argparse
import sys

# Asegurar compatibilidad UTF-8 en consolas Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass


def generate_trace_table(variables: list[str], steps: int = 4) -> str:
    """Genera una tabla Markdown para prueba de escritorio paso a paso."""
    headers = ["Paso / Iteración", "Línea"] + [f"Var `{v.strip()}`" for v in variables] + ["Condición Evaluada", "Salida / Efecto"]
    separator = [":---"] * len(headers)

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(separator) + " |"
    ]

    for step in range(1, steps + 1):
        row = [f"Paso {step}", f"L{step+2}"] + ["..."] * len(variables) + ["True / False", "-"]
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def generate_flowchart(template_type: str) -> str:
    """Genera plantillas de diagramas de flujo Mermaid estándar."""
    templates = {
        "if_else": """```mermaid
flowchart TD
    Start(["Inicio"]) --> Input[/"Leer dato"/]
    Input --> Cond{"¿Condición?"}
    Cond -- Sí / True --> BlockTrue["Rama Verdadera"]
    Cond -- No / False --> BlockFalse["Rama Falsa"]
    BlockTrue --> Merge["Continuar flujo"]
    BlockFalse --> Merge
    Merge --> EndNode(["Fin"])
```""",

        "while_loop": """```mermaid
flowchart TD
    Start(["Inicio"]) --> Init["Inicializar variables"]
    Init --> Cond{"¿Condición de parada?"}
    Cond -- Sí (Continuar) --> Body["Cuerpo del bucle<br/>(Cálculos / Proceso)"]
    Body --> Update["Actualizar variable de control"]
    Update --> Cond
    Cond -- No (Terminar) --> Output[/"Mostrar resultado"/]
    Output --> EndNode(["Fin"])
```""",

        "for_range": """```mermaid
flowchart TD
    Start(["Inicio"]) --> Init["i = inicio"]
    Init --> Check{"¿i < fin?"}
    Check -- Sí --> Body["Ejecutar iteración con i"]
    Body --> Inc["i = i + paso"]
    Inc --> Check
    Check -- No --> EndNode(["Fin del bucle"])
```""",

        "linear_search": """```mermaid
flowchart TD
    Start(["Inicio: Buscar objetivo X"]) --> Init["i = 0, encontrado = False"]
    Init --> Check{"¿i < longitud y no encontrado?"}
    Check -- Sí --> Compare{"¿arreglo[i] == X?"}
    Compare -- Sí --> Found["encontrado = True<br/>posicion = i"]
    Found --> Check
    Compare -- No --> Next["i = i + 1"]
    Next --> Check
    Check -- No --> Result{"¿encontrado == True?"}
    Result -- Sí --> ShowFound[/"Elemento hallado en pos"/]
    Result -- No --> ShowNotFound[/"Elemento no encontrado"/]
    ShowFound --> EndNode(["Fin"])
    ShowNotFound --> EndNode
```"""
    }

    return templates.get(template_type, f"Plantilla desconocida '{template_type}'. Opciones: {list(templates.keys())}")


def main():
    parser = argparse.ArgumentParser(description="Generador de tablas de traza y diagramas Mermaid.")
    parser.add_argument("--type", choices=["trace", "flowchart"], required=True, help="Tipo de recurso a generar")
    parser.add_argument("--vars", type=str, default="i,contador,total", help="Variables separadas por coma para la traza")
    parser.add_argument("--steps", type=int, default=4, help="Número de pasos en la traza")
    parser.add_argument("--template", choices=["if_else", "while_loop", "for_range", "linear_search"], default="while_loop", help="Plantilla Mermaid")

    args = parser.parse_args()

    if args.type == "trace":
        var_list = [v.strip() for v in args.vars.split(",") if v.strip()]
        print(generate_trace_table(var_list, args.steps))
    elif args.type == "flowchart":
        print(generate_flowchart(args.template))


if __name__ == "__main__":
    main()
