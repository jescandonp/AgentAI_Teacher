# Hoja de Ruta al Segundo Parcial — Juan Diego Coronado (C++, Javeriana)

**Preparada para:** Juan Manuel Escandón (tutor)  
**Fecha:** sábado 3 de octubre de 2026 · **Parcial:** lunes 5 de octubre de 2026 (formato **en papel**)  
**Sesiones de tutoría:** solo dos, **sábado 3 y domingo 4**. El lunes no hay sesión (solo calentamiento autónomo).  
**Fuentes:** programa oficial del curso *Introducción a la Programación* (Javeriana), diapositivas de Clase 6, código de clase y el PDF *Tareas-Refuerzo-CPP-Juan-Diego*.

> **Supuesto a confirmar:** por los temas que indicas (funciones, matrices, ordenamientos, acumulativo), el lunes es el **Segundo Parcial Conjunto (20 %, semana 10, RAE 2)**. Según el programa, evalúa condicionales, ciclos y funciones (modularidad, paso de parámetros y alcance/scope). Como es acumulativo, incluye también todo el Primer Parcial.

---

## 1. Alcance del parcial (según el programa oficial)

| Bloque | Temas | Clases / Talleres |
| :--- | :--- | :--- |
| **A. Acumulativo (Parcial 1)** | Proceso de solución, compilación y depuración · tipos, variables, E/S · condicionales simples, dobles, anidados y `switch` · ciclos `while`, `do-while`, `for` · contadores, acumuladores, banderas, centinela · mayor/menor · ciclos anidados | Clases 1-12, Talleres 01-04 |
| **B. Funciones** | Definición, firma, prototipos, modularidad · paso de parámetros (valor y referencia) · alcance (*scope*) | Clase 13, Taller 05 |
| **C. Arreglos 1D** | Declaración, recorrido, arreglos paralelos, paso a funciones | Clase 15, Taller 06 |
| **D. Búsqueda y ordenamiento** | Búsqueda secuencial y binaria · ordenamiento (burbuja y selección) | Clase 17, Taller 07 |
| **E. Matrices 2D** | Recorrido por filas y columnas, operaciones | Clases 19-20, Taller 08 |

**Fuera de alcance del lunes:** funciones con matrices (Clase 21), `struct` y archivos de texto. Son del Tercer Parcial.

---

## 2. Diagnóstico de partida (con evidencia de su código)

| Tema | Estado | Evidencia |
| :--- | :--- | :--- |
| E-P-S y secciones comentadas | Dominado | `main_for_v2.cpp` |
| Acumulador en `for`, `if / else if / else` | Dominado | `main_for_v2.cpp:29-56` |
| Funciones con arreglo y retorno `-1` | Sólido | `mostrar` y `buscar` en `jddd.cpp:66-84` |
| **Límites del arreglo** | **Crítico** | `jddd.cpp:38` usa `i <= TAM` y lee `datos[10]` |
| **Índices sobre `string`** | **Crítico** | `jddd.cpp:59-61` recorre `palabra[i]` hasta `TAM-1` |
| Constante vs número escrito a mano | Por reforzar | `mostrar(datos, 10)`, `buscar(datos, 10, 30)` |
| `while`, `do-while`, centinela, ciclos anidados | **Sin evidencia** | no hay código suyo con estos temas |
| Paso por valor / referencia, scope | **Sin evidencia** | solo usa funciones con arreglos |
| Búsqueda binaria, ordenamiento (burbuja/selección) | **Sin evidencia** | no aparece en su código |
| Matrices 2D | **Sin evidencia** | no aparece en su código |

**Lectura del tutor:** lo que domina es el núcleo del Parcial 1. El riesgo está en los temas nuevos (D y E) y en dos errores de límites que ya tiene identificados. Con dos días y formato en papel, el plan prioriza lo que no tiene evidencia y entrena escribir código a mano.

---

## 3. Revisión de las tareas de hoy (guion para el tutor)

Orden sugerido: 10 min por ejercicio. Regla del PDF: **lo corre, lo explica en voz alta y le piden un cambio en vivo.** Como el parcial es en papel, además le pides que **escriba a mano** la función más difícil de cada ejercicio.

### Cómo revisar cada entrega

1. **Antes de ejecutar**, buscar `<=` contra `TAM`, acumuladores sin inicializar y números `8` / `10` / `5` escritos a mano.
2. **Ejecutar** con los casos del PDF (verificados a mano, las cuentas coinciden).
3. **Romperlo a propósito:** nota `5.5`, nota `-1`, código `999`, 4 unidades de un producto con stock 3.
4. **Pedir el cambio en vivo** (en un programa bien hecho es de una línea).

### Ejercicio 1: Sensores

| Caso | Entrada | Esperado |
| :--- | :--- | :--- |
| Principal | 36.5 · 12.0 · 20.0 · 35.0 · 14.9 · 28.5 · 40.1 · 15.0 | Promedio 25.25 · 3 críticas · 2 bajas |
| Bordes | 35.0 y 15.0 | 35.0 sí es crítica · 15.0 no es baja |

- **Errores probables:** `> 35.0` en lugar de `>= 35.0`; `<= 15.0` en lugar de `< 15.0`; `suma` sin inicializar; `i <= TAM`.
- **Cambio en vivo:** "Ahora son 12 sensores" (debe tocar solo `const int TAM = 12;`).
- **Pregunta socrática:** *¿Qué hay en `temperaturas[8]` si `TAM = 8`?*

### Ejercicio 2: Notas

| Caso | Entrada | Esperado |
| :--- | :--- | :--- |
| Principal | 3.5 · 4.2 · 2.8 · 5.0 · 3.0 · 4.8 · 1.5 · 3.5 · 4.0 · 2.7 | Promedio 3.50 · mejor 5.0, índice 3 |
| Buscar 3.5 | | Índice 0 (la primera) |
| Buscar 4.5 | | −1 → "no está" |
| Ingresar 5.5 o −1 | | Rechaza y vuelve a pedir |

- **Errores probables:** `return -1;` dentro del bucle; máximo inicializado en 0; comparar `double` con `==`.
- **Cambio en vivo:** "Agrega una función que cuente cuántos aprobaron (≥ 3.0)".
- **Pregunta socrática:** *¿Por qué `mostrarNotas` recibe `const` e `ingresarNotas` no?*

### Ejercicio 3: Facturación

| Carrito | Subtotal | Descuento | IVA | Total |
| :--- | ---: | ---: | ---: | ---: |
| 102 × 2 · 105 × 3 | 165.000 | 16.500 (10 %) | 28.215 | 176.715 |
| 103 × 1 · 102 × 1 · 105 × 1 | 150.000 | 7.500 (5 %) | 27.075 | 169.575 |
| 101 × 5 | 75.000 | 3.750 (5 %) | 13.537,5 | 84.787,5 |
| 105 × 2 · 101 × 1 | 65.000 | 0 | 12.350 | 77.350 |

Rechazos: agregar 104 × 4 → "solo hay 3" · código 999 → "Producto no existe". Producto estrella del caso 1: 105 (3 unidades). Stock tras el caso 1: 102 = 6, 105 = 9.

- **Errores probables:** IVA antes del descuento; el borde de $150.000 que debe dar 5 %; no descontar `stock[i]`; `break;` faltante en el `switch`.
- **Cambio en vivo:** "Agrega un sexto producto" o "el umbral del 10 % pasa a $200.000".
- **Pregunta socrática:** *¿Qué se rompe si ordenas solo `precios[]` y no los otros tres arreglos?* (conecta con ordenamiento de arreglos paralelos).

### Registro de la sesión
Al terminar, registrar con `execution/student_tracker.py` el resultado y los errores observados, y marcar los checkpoints de la sección 4.

---

## 4. Ruta de estudio guiada: 2 sesiones, 8 checkpoints

Los **CP1, CP2 y CP3 ya tuvieron repaso** en sesiones anteriores, así que hoy se arranca en el **CP4**. Esos tres se verifican con un chequeo relámpago el domingo, sin gastar tiempo de sesión en reexplicarlos. Cada checkpoint tiene un **criterio de paso observable en papel**: si no se cumple, se hace el refuerzo y se repite el criterio antes de avanzar. Nunca se entrega la solución antes de que él la plantee con E-P-S o con traza.

> **Supuesto de duración:** ≈ 3 h el sábado y ≈ 2,5 h el domingo. Los tiempos por bloque permiten recortar si la sesión es más corta (ver *Recortes*).

### Resumen

| Cuándo | Checkpoints | Foco |
| :--- | :--- | :--- |
| ✅ Antes | CP1, CP2, CP3 | Base acumulativa, límites, funciones y scope (repasados; se verifican el domingo) |
| **Sábado 3-oct** | **CP4, CP5, CP6** | Revisión de tareas, arreglos con funciones, búsqueda binaria, ordenamiento |
| **Domingo 4-oct** | Chequeo CP1-3, **CP7, CP8** | Matrices, simulacro en papel y corrección |
| Lunes 5-oct (sin sesión) | Calentamiento autónomo | 20 min antes del parcial |

### Sesión 1 · Sábado 3-oct (≈ 3 h): *Arreglos con funciones, búsqueda y ordenamiento*

| Min | Bloque | Qué se hace |
| :-- | :--- | :--- |
| 0-30 | **Revisión de las tareas** (sección 3) | Ej1 y Ej2 en 10 min cada uno; Ej3 en 10 min. Las funciones del Ej2 son la evidencia del **CP4** |
| 30-50 | **CP4**: arreglos y paralelos con funciones | Escribe a mano `buscar` (retorna `-1` después del bucle) y `obtenerMayor` (con `maximo = v[0]`) y las llama desde `main` |
| 50-90 | **CP5**: búsqueda secuencial y binaria | Traza la binaria sobre `{2,5,8,12,16,23,38,56,72,91}` buscando 23 (pregunta 5) y explica por qué exige el arreglo ordenado |
| 90-155 | **CP6**: ordenamiento (burbuja 40 min, selección 25 min) | Traza burbuja sobre `{5,2,4,1}` (pregunta 6) y escribe el código de **uno** de los dos a mano, sin ayudas |
| 155-180 | **Cierre** | Registrar en `student_tracker.py`; entregar la tarea de la noche |

| CP | Criterio de paso (en papel) | Refuerzo si falla |
| :--- | :--- | :--- |
| **CP4** | `buscar` y `obtenerMayor` escritas a mano, con prototipos, probadas con `{3, 7, 7, 2}` buscando 7 | Trazar la búsqueda: ¿en qué iteración sale el `return`? |
| **CP5** | Traza completa de la binaria (valores de `bajo`, `alto`, `medio` y 3 comparaciones) | Marcar los tres índices sobre una tira de casillas |
| **CP6** | Traza de burbuja correcta (5 intercambios) y código de un ordenamiento sin ayudas | Con fichas de papel numeradas, ordenar a mano antes de escribir el código; luego traducir cada movimiento |

**Refuerzos de contenido:**
- **Burbuja:** compara vecinos y los intercambia; tras cada pasada el mayor queda al final. Dos bucles: `for (i = 0; i < n-1; i++)` y `for (j = 0; j < n-1-i; j++)`. Error típico: dejar el límite de `j` en `n-1` y leer `v[j+1]` fuera de rango (mismo error de límites que en CP2).
- **Selección:** busca el índice del mínimo del tramo `[i, n)` y lo intercambia con la posición `i`.
- **Intercambio:** requiere una variable auxiliar (`aux = a; a = b; b = aux;`). Sin ella se pierde un valor.
- **Binaria:** `medio = (bajo + alto) / 2`; si `v[medio] < x` entonces `bajo = medio + 1`, si no `alto = medio - 1`; termina cuando `bajo > alto`.
- **Conexión con el Ej3:** si se ordena un arreglo paralelo, hay que mover `codigos[]`, `precios[]` y `stock[]` con el mismo intercambio.

**Tarea de la noche (≈ 45 min, en papel):** escribir de memoria burbuja y búsqueda binaria; rehacer las preguntas 5 y 6 del banco sin mirar la clave. Traer las hojas el domingo.

### Sesión 2 · Domingo 4-oct (≈ 2,5 h): *Matrices y simulacro*

| Min | Bloque | Qué se hace |
| :-- | :--- | :--- |
| 0-15 | **Chequeo relámpago CP1-CP3** | Preguntas 1, 3 y 4 del banco, 5 min cada una. Si falla alguna, anotar para la corrección final |
| 15-25 | **Revisión de la tarea de la noche** | Escribe burbuja a mano de memoria; se corrige en vivo |
| 25-75 | **CP7**: matrices 2D | Ver abajo |
| 75-135 | **CP8**: simulacro cronometrado | Preguntas 1-8 del banco, en papel y sin ayudas |
| 135-150 | **Corrección y focos** | Corregir con la clave, nombrar las 2 debilidades que quedan y fijar el calentamiento del lunes |

| CP | Criterio de paso (en papel) | Refuerzo si falla |
| :--- | :--- | :--- |
| **CP7** | Dada `int m[3][3]`, escribe el doble `for` que la muestra y los que calculan la suma de cada fila, de cada columna y de la diagonal (pregunta 7) | Dibujar la cuadrícula con índices `[fila][columna]` y numerar el orden de visita del doble bucle |
| **CP8** | Resuelve el simulacro en el tiempo fijado, sin ayudas; ningún `<=` contra el tamaño, acumuladores inicializados, prototipos presentes | Revisar con la lista de chequeo de papel (abajo) |

**Refuerzos de contenido (matrices):**
- La fila es el índice **externo** y la columna el **interno**: `for (i = 0; i < FIL; i++) for (j = 0; j < COL; j++) m[i][j]`.
- Para recorrer **por columnas** se invierte el orden de los bucles (el de columnas es el externo).
- La diagonal principal es `m[i][i]`; la secundaria, `m[i][COL-1-i]` (solo en matrices cuadradas).
- Funciones con matrices son del Tercer Parcial; en este solo se pide declarar y recorrer.

### Lunes 5-oct (sin sesión): calentamiento autónomo de 20 min

1. Leer en voz alta la lista de chequeo de papel (abajo).
2. Escribir a mano, de memoria: burbuja, el doble `for` de una matriz y `buscar` con `-1`.
3. Repasar los dos puntos débiles anotados en la corrección del domingo.

No estudiar temas nuevos ese día.

### Recortes si la sesión se queda corta

| Situación | Recorte |
| :--- | :--- |
| El sábado se alarga | Hacer solo **burbuja** en CP6 y pasar selección al domingo (10 min en el bloque de revisión) |
| La revisión de tareas consume más de 30 min | Revisar a fondo solo Ej2 (funciones y arreglos) y dejar Ej1 y Ej3 para el domingo en 5 min cada uno |
| El domingo se alarga | Simulacro solo con las preguntas **5-8** (los temas nuevos), y las 1-4 como tarea corta para el lunes |
| Falla el chequeo de CP2 o CP3 | Prioridad sobre CP7: son errores que ya le han costado en su código |

### Estrategia específica para parcial en papel

| Práctica | Por qué |
| :--- | :--- |
| Escribir a mano `#include <iostream>` y `using namespace std;` al inicio de cada programa | En papel no hay compilador que avise, y es un punto que se pierde por descuido |
| Prototipos arriba del `main` y funciones debajo | Es lo que se evalúa en "modularidad" |
| Llaves y `;` revisados al final | El compilador no corrige la sintaxis |
| Hacer primero el E-P-S en una esquina de la hoja y luego el código | Ordena el razonamiento y suma puntos de diseño |
| Dejar trazas visibles (tabla de variables por iteración) | Permite rescatar puntaje parcial si el código falla |
| Revisión final: ¿algún `<=` contra el tamaño?, ¿acumulador inicializado?, ¿`return` en todos los caminos? | Los tres errores más frecuentes de su historial |

---

## 5. Banco de práctica tipo parcial (simulacro del domingo, en papel)

Todas se resuelven primero en papel; la clave solo se usa después de que él explique su razonamiento.

**Bloque A: acumulativo y funciones**

1. **Traza (10 pts).** ¿Qué imprime? ¿Hay comportamiento indefinido?
   ```cpp
   int v[4] = {2, 4, 6, 8};
   int suma = 0;
   for (int i = 0; i <= 4; i++) suma += v[i];
   cout << suma;
   ```
2. **Encuentra el error (10 pts).** La función debe devolver el índice de la primera ocurrencia o `-1`. Falla con `{1, 2, 3}` buscando `3`:
   ```cpp
   int buscar(int v[], int n, int x) {
       for (int i = 0; i < n; i++) {
           if (v[i] == x) return i;
           else return -1;
       }
   }
   ```
3. **Ciclos anidados (10 pts).** ¿Qué imprime?
   ```cpp
   for (int i = 1; i <= 3; i++) {
       for (int j = 1; j <= i; j++) cout << j;
       cout << endl;
   }
   ```
4. **Valor vs referencia y scope (10 pts).** ¿Qué imprime?
   ```cpp
   void f(int a, int &b) { a++; b++; }
   int main() {
       int x = 1, y = 1;
       f(x, y);
       cout << x << y;
   }
   ```

**Bloque B: búsqueda, ordenamiento y matrices**

5. **Búsqueda binaria (10 pts).** En `{2,5,8,12,16,23,38,56,72,91}`, traza la búsqueda de `23`: valores de `bajo`, `alto`, `medio` en cada paso y número de comparaciones.
6. **Ordenamiento (10 pts).** Traza burbuja sobre `{5,2,4,1}`: estado del arreglo tras cada pasada y total de intercambios.
7. **Matriz (15 pts).** Dada `int m[3][3] = {{1,2,3},{4,5,6},{7,8,9}};` escribe el código que imprime la suma de cada fila y la suma de la diagonal principal, y di qué imprime.
8. **Programa completo (25 pts).** E-P-S y código: leer `TAM = 6` precios, ordenarlos de menor a mayor (a elección: burbuja o selección), aplicar 10 % de descuento si el subtotal supera $100.000, sumar IVA del 19 % y mostrar el más caro y el más barato. Debe usar al menos una función con prototipo.

**Clave para el tutor**

| # | Respuesta | Nota |
| :-- | :--- | :--- |
| 1 | Lee `v[4]`, fuera de rango: comportamiento indefinido. Resultado no garantizado (20 más basura) | Es el error central del bloque |
| 2 | Devuelve `-1` en la primera iteración con `{1,2,3}` buscando 3. Corrección: `return -1;` después del bucle | También falta `return` si `n == 0` |
| 3 | `1` / `12` / `123` (una línea por cada `i`) | |
| 4 | `12`: `a` es copia, `b` es referencia | `x` queda en 1, `y` pasa a 2 |
| 5 | `bajo=0, alto=9, medio=4` (16 < 23) → `bajo=5, alto=9, medio=7` (56 > 23) → `bajo=5, alto=6, medio=5` (23, encontrado). 3 comparaciones | |
| 6 | Pasada 1: `2,4,1,5` · Pasada 2: `2,1,4,5` · Pasada 3: `1,2,4,5` · **5 intercambios** | Coincide con las 5 inversiones del arreglo original |
| 7 | Filas: 6, 15, 24 · Diagonal: 1+5+9 = 15 | Columnas: 12, 15, 18 (pregunta extra) |
| 8 | Rúbrica: E-P-S (5) · lectura con `i < TAM` (3) · ordenamiento correcto (7) · descuento antes que IVA (4) · mayor y menor (3) · función con prototipo (3) | Total 25 |

---

## 6. Decisiones abiertas para JuanMa

1. **Confirmar que el lunes es el Segundo Parcial** (semana 10). Si fuera otro, el alcance de la sección 1 cambia.
2. **Duración de cada sesión y del parcial.** Asumí ≈ 3 h el sábado y ≈ 2,5 h el domingo; si son más cortas, aplica la tabla de recortes.
3. **¿El parcial permite hoja de apuntes?** Cambia cuánto debe memorizar el ordenamiento y la búsqueda binaria.
4. **Script de revisión automática** de las tareas: se entrega junto a esta hoja de ruta en `execution/`. Esta máquina no tiene compilador de C++, así que hay que correrlo donde exista `g++`, `clang++` o `cl`.
