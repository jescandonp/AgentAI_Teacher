# SOP: Evaluación de Código y Diagnóstico de Errores (Evaluation & Debugging SOP)

## 1. Objetivo
Establecer un procedimiento riguroso y determinista para recibir código escrito por los estudiantes, identificar la raíz exacta del problema (sintáctico, lógico, de tipos, de memoria o de límites) y estructurar un feedback constructivo y formativo.

---

## 2. Taxonomía de Errores en Fundamentos de Programación

| Categoría de Error | Descripción | Manifestación en Python | Manifestación en C++ |
| :--- | :--- | :--- | :--- |
| **Sintaxis** | Violación de las reglas gramaticales del lenguaje. | `SyntaxError`, `IndentationError`. | Error de compilación: falta `;`, llaves `{}` no balanceadas, includes faltantes. |
| **Tipos** | Operaciones entre tipos incompatibles o conversiones no válidas. | `TypeError` (ej: concatenar `str` + `int`). | Error de compilación: `cannot convert 'T1' to 'T2'`, pérdida de precisión. |
| **Lógica** | El código compila/ejecuta pero produce un resultado incorrecto. | Salida equivocada, acumuladores mal inicializados, condición invertida. | Igual que Python; variables no inicializadas con valores residuales. |
| **Límites / Off-by-One** | Iteraciones de más o de menos, acceso a índices fuera de rango. | `IndexError: list index out of range`. | Undefined behavior / `Segmentation fault` / lectura de memoria ajena. |
| **Ciclos Infinitos** | Condición de parada que nunca se satisface. | Proceso congelado, `KeyboardInterrupt`. | Proceso congelado, alto consumo de CPU. |
| **Ámbito / Scope** | Uso de variables fuera de su bloque de definición. | `UnboundLocalError`, `NameError`. | Error de compilación: `'variable' was not declared in this scope`. |
| **Flujo de Entrada/Salida** | Problemas al leer datos del usuario o formatear salida. | `ValueError` en `int(input())`. | Buffer atascado por `\n`, tipos incompatibles en `cin >>`. |

---

## 3. Protocolo de Diagnóstico Paso a Paso

1. **Paso 1: Validación Estática / Compilación**
   - Ejecutar la herramienta `execution/code_checker.py` o revisar la estructura del código.
   - Detectar si el fallo ocurre en tiempo de compilación/parseo o en tiempo de ejecución.

2. **Paso 2: Aislamiento del Punto de Falla y Consulta de Base de Conocimiento**
   - Ubicar el número de línea exacto y el estado de las variables involucradas antes de esa línea.
   - En caso de errores sutiles (variables sin inicializar / UB en C++, o mutabilidad / aliasing / default arguments en Python), contrastar con las bases de conocimiento en `resources/knowledge/cpp/` o `resources/knowledge/python/`.

3. **Paso 3: Construcción de Prueba de Escritorio (Traza)**
   - Elaborar una tabla de traza con un conjunto de datos pequeño (ej. un arreglo de 3 elementos o un número simple como `n = 4`).
   - Mostrar qué valores van tomando las variables en cada paso/iteración.

4. **Paso 4: Formulación del Feedback al Estudiante**
   - **Reconocer lo que está bien:** Validar la intención y las partes correctas de la solución.
   - **Explicar el síntoma:** Qué está pasando frente a qué se esperaba que pasara.
   - **Aplicar la pista correspondiente (Nivel 1 a 4 según `directives/tutor_pedagogia_sop.md`).**

---

## 4. Estructura de Respuesta para Debugging

Al responder a un estudiante con un error en su código, usar la siguiente estructura visual:

```markdown
### 🔍 Diagnóstico de tu Código

- **Estado:** ⚠️ Error de Lógica / ❌ Error de Sintaxis / 🛑 Error en Tiempo de Ejecución
- **Línea clave:** Línea X
- **¿Qué está sucediendo?** (Explicación conceptual sin jerga excesiva)

#### 📋 Prueba de Escritorio (Valores paso a paso)
| Paso / Iteración | Variable A | Variable B | Condición Evaluada | Resultado |
| :--- | :--- | :--- | :--- | :--- |
| Inicio | ... | ... | ... | ... |
| Iteración 1 | ... | ... | ... | ... |

#### 💡 Pregunta para pensar (Pista Nivel 1/2)
- ¿Qué ocurre en la iteración 2 cuando la variable llega a...?
```
