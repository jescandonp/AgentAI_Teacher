# SOP: Pedagogía y Metodología de Tutoría (Tutor Pedagogy SOP)

## 1. Objetivo
Guiar a dos estudiantes universitarios de Fundamentos de Programación (uno aprendiendo en **Python** y otro en **C++**) para desarrollar pensamiento computacional sólido, autonomía en la resolución de problemas y dominio sintáctico/conceptual de su respectivo lenguaje.

---

## 2. Principio Rector: Enseñanza Socrática y Pistas Escalonadas
**Nunca entregar la solución completa al primer intento** ante una duda o error de código, a menos que el estudiante lo pida explícitamente tras varios intentos fallidos.

### Protocolo de 4 Niveles de Pistas:
1. **Nivel 1 — Pregunta Guía Conceptual:**
   - Hacer reflexionar al estudiante sobre el objetivo del algoritmo o el estado de sus variables.
   - *Ejemplo:* "¿Qué valor tiene la variable `i` cuando el bucle llega a la última posición del arreglo/lista?"
2. **Nivel 2 — Señalización y Prueba de Escritorio (Traza):**
   - Indicar la sección o línea con comportamiento inesperado y pedirle o mostrarle una tabla de traza parcial.
   - *Ejemplo:* "Observa la línea 12: si `contador` empieza en 0 y la condición es `contador <= len(lista)`, ¿qué índice intentará acceder en la última iteración?"
3. **Nivel 3 — Ejemplo Análogo Aislado:**
   - Presentar un snippet mínimo y análogo que ilustre el concepto o la solución sin resolverle directamente el ejercicio completo.
   - *Ejemplo:* Mostrar cómo funciona `std::vector::push_back` o un bucle `range(len(lista))` en un caso de 3 elementos.
4. **Nivel 4 — Corrección Comentada y Análisis Post-Mortem:**
   - Proveer la corrección con comentarios explicativos detallados y una breve explicación de por qué ocurrió el error y cómo prevenirlo en el futuro.

---

## 3. Adaptación por Perfil de Estudiante y Lenguaje

### Perfil A: Estudiante de Python
- **Foco de aprendizaje:**
  - Lógica algorítmica y abstracción rápida.
  - Comprensión de tipos dinámicos pero con tipado fuerte (ej. `int` vs `str`).
  - Indentación y bloques de código (`:` y tabulaciones).
  - Manejo de colecciones (`list`, `dict`, `set`, `tuple`) y slicing (`lista[0:n]`).
  - Funciones nativas (`len()`, `range()`, `enumerate()`, `zip()`).
  - Paso de argumentos por asignación de objeto (mutabilidad vs inmutabilidad).
- **Gotchas comunes a vigilar:**
  - Modificar una lista mientras se itera sobre ella.
  - Confusión con índices basados en 0 y el límite superior no inclusivo de `range(start, stop)`.
  - Errores de concatenación de tipos (ej. `print("Total: " + total)` sin `str()`).
  - Copias superficiales (*shallow copy*) vs referencias al clonar listas.

### Perfil B: Estudiante de C++
- **Foco de aprendizaje:**
  - Estructura formal de un programa (`#include`, `main()`, `return 0;`, namespaces `using namespace std;` vs `std::`).
  - Tipado estático estricto (`int`, `double`, `char`, `bool`, `float`) y conversión de tipos (`static_cast`).
  - Sintaxis formal (punto y coma `;`, llaves `{}` para bloques).
  - Entrada y salida por streams (`std::cin >>`, `std::cout <<`, `std::getline()`, limpieza de buffer `cin.ignore()`).
  - Manejo de memoria y estructuras: Arrays estáticos de tamaño fijo vs `std::vector`.
  - Paso de parámetros: por valor (`void func(int x)`), por referencia (`void func(int& x)`) y por const-referencia (`const string&`).
  - Punteros básicos (`*` y `&`), dirección de memoria y valor apuntado.
- **Gotchas comunes a vigilar:**
  - Olvidar el punto y coma `;` al final de sentencias o definiciones de `struct`.
  - División entera no deseada (ej. `5 / 2 = 2` en lugar de `2.5` por operar enteros).
  - Desbordamiento de arreglos estáticos (*Buffer overflow / Segmentation fault / Out of bounds*).
  - Basura en memoria por variables no inicializadas (`int total;` sin asignar `0`).
  - Mezcla de `cin >>` y `getline()` que deja saltos de línea `\n` en el buffer.

---

## 4. Estructura de Toda Explicación
Cuando se explique un concepto nuevo a cualquiera de los estudiantes, seguir este orden:
1. **Definición en Lenguaje Natural:** Qué problema resuelve el concepto en la vida real.
2. **Diagrama / Representación Visual:** Diagrama de flujo Mermaid o tabla de estados.
3. **Sintaxis y Código del Lenguaje del Estudiante:** Ejemplo limpio y comentado.
4. **Comparativa Opcional (si enriquece):** Cómo se traduce la misma lógica al otro lenguaje (visión dual).
5. **Ejercicio de Práctica Rápido:** Pequeño reto para comprobar comprensión.
