"""
code_checker.py - Validador y diagnosticador determinista de código para estudiantes.

Soporta análisis sintáctico y de patrones comunes para Python y C++.
Uso:
    python code_checker.py --lang python --code "x = 10\nprint(x)"
    python code_checker.py --lang cpp --file ruta/al/archivo.cpp
"""

import ast
import argparse
import json
import re
import sys

# Asegurar compatibilidad UTF-8 en consolas Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass


def check_python_code(code: str) -> dict:
    """Verifica código Python usando AST y reglas deterministas."""
    result = {
        "language": "python",
        "valid": True,
        "errors": [],
        "warnings": [],
        "metrics": {
            "total_lines": len(code.splitlines()),
            "functions": 0,
            "loops": 0,
            "conditionals": 0
        }
    }

    # 1. Chequeo sintáctico mediante AST
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        result["valid"] = False
        result["errors"].append({
            "type": "SyntaxError",
            "line": e.lineno,
            "offset": e.offset,
            "message": str(e.msg),
            "text": e.text.strip() if e.text else ""
        })
        return result
    except Exception as e:
        result["valid"] = False
        result["errors"].append({
            "type": type(e).__name__,
            "line": 0,
            "message": str(e)
        })
        return result

    # 2. Análisis estático básico de patrones
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            result["metrics"]["functions"] += 1
        elif isinstance(node, (ast.For, ast.While)):
            result["metrics"]["loops"] += 1
        elif isinstance(node, (ast.If, ast.IfExp)):
            result["metrics"]["conditionals"] += 1

        # Advertencia: modificación de lista durante iteración
        if isinstance(node, ast.For) and isinstance(node.target, ast.Name):
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Call) and isinstance(subnode.func, ast.Attribute):
                    if subnode.func.attr in ['append', 'remove', 'pop', 'extend']:
                        if isinstance(subnode.func.value, ast.Name) and isinstance(node.iter, ast.Name):
                            if subnode.func.value.id == node.iter.id:
                                result["warnings"].append({
                                    "line": getattr(subnode, 'lineno', 0),
                                    "type": "DangerousMutation",
                                    "message": f"Modificando la lista '{node.iter.id}' mientras se itera sobre ella."
                                })

    return result


def check_cpp_code(code: str) -> dict:
    """Verifica código C++ mediante análisis léxico y de patrones comunes de estudiantes."""
    result = {
        "language": "cpp",
        "valid": True,
        "errors": [],
        "warnings": [],
        "metrics": {
            "total_lines": len(code.splitlines()),
            "has_main": False,
            "has_iostream": False,
            "uses_std": False
        }
    }

    lines = code.splitlines()

    # 1. Chequeo de llaves y paréntesis balanceados
    stack = []
    for i, line in enumerate(lines, 1):
        # Limpiar strings y comentarios para evitar falsos positivos
        clean_line = re.sub(r'//.*', '', line)
        clean_line = re.sub(r'".*?"', '', clean_line)
        clean_line = re.sub(r"'.*?'", '', clean_line)

        for char in clean_line:
            if char in '({[':
                stack.append((char, i))
            elif char in ')}]':
                if not stack:
                    result["valid"] = False
                    result["errors"].append({
                        "type": "UnbalancedBracket",
                        "line": i,
                        "message": f"Cierre inesperado '{char}' sin apertura correspondiente."
                    })
                else:
                    top_char, top_line = stack.pop()
                    expected = {'(': ')', '{': '}', '[': ']'}[top_char]
                    if char != expected:
                        result["valid"] = False
                        result["errors"].append({
                            "type": "MismatchedBracket",
                            "line": i,
                            "message": f"Se esperaba '{expected}' para cerrar '{top_char}' abierto en línea {top_line}, pero se encontró '{char}'."
                        })

    while stack:
        top_char, top_line = stack.pop()
        result["valid"] = False
        result["errors"].append({
            "type": "UnclosedBracket",
            "line": top_line,
            "message": f"Apertura '{top_char}' en línea {top_line} nunca fue cerrada."
        })

    # 2. Búsqueda de elementos estructurales
    has_iostream = bool(re.search(r'#include\s*<iostream>', code))
    has_main = bool(re.search(r'int\s+main\s*\(', code))
    uses_namespace_std = bool(re.search(r'using\s+namespace\s+std\s*;', code))

    result["metrics"]["has_iostream"] = has_iostream
    result["metrics"]["has_main"] = has_main
    result["metrics"]["uses_std"] = uses_namespace_std

    if not has_main:
        result["warnings"].append({
            "line": 0,
            "type": "MissingMain",
            "message": "No se encontró la función obligatoria 'int main()'."
        })

    # 3. Detección de uso de cout/cin sin std:: ni using namespace std
    for i, line in enumerate(lines, 1):
        clean_line = re.sub(r'//.*', '', line)
        if not uses_namespace_std:
            if re.search(r'\b(cout|cin|endl|string|vector)\b', clean_line) and not re.search(r'\bstd::', clean_line):
                result["warnings"].append({
                    "line": i,
                    "type": "NamespaceScopeWarning",
                    "message": f"Uso de elementos de la biblioteca estándar en línea {i} sin prefijo 'std::' ni 'using namespace std;'."
                })

        # Chequeo heurístico de punto y coma faltante en sentencias típicas
        stripped = clean_line.strip()
        if stripped and not stripped.startswith(('#', '//', '/*', '*', 'for', 'if', 'while', 'switch', 'else', '{', '}')):
            if not stripped.endswith((';', '{', '}', ':', ',')):
                # Posible falta de punto y coma
                result["warnings"].append({
                    "line": i,
                    "type": "PossibleMissingSemicolon",
                    "message": f"La línea {i} ('{stripped[:30]}...') podría carecer de punto y coma ';' al final."
                })

    return result


def main():
    parser = argparse.ArgumentParser(description="Validador determinista de código para tutoría.")
    parser.add_argument("--lang", choices=["python", "cpp"], required=True, help="Lenguaje de programación")
    parser.add_argument("--code", type=str, help="Código como string directo")
    parser.add_argument("--file", type=str, help="Ruta al archivo con el código")

    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                code_content = f.read()
        except Exception as e:
            print(json.dumps({"valid": False, "error": f"Error al leer archivo: {e}"}, indent=2))
            sys.exit(1)
    elif args.code:
        code_content = args.code
    else:
        print(json.dumps({"valid": False, "error": "Debe proporcionar --code o --file"}, indent=2))
        sys.exit(1)

    if args.lang == "python":
        analysis = check_python_code(code_content)
    else:
        analysis = check_cpp_code(code_content)

    print(json.dumps(analysis, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
