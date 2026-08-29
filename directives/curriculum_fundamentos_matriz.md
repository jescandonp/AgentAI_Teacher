# Matriz Curricular: Fundamentos de Programación (Python vs C++)

Esta matriz define el plan de estudios fundamental para ambos estudiantes, alineando los conceptos algorítmicos universales con la implementación sintáctica en Python y C++.

---

## Módulo 1: Variables, Tipos de Datos y Operadores

| Concepto Algorítmico | Implementación en Python | Implementación en C++ | Conceptos Clave & Diferencias |
| :--- | :--- | :--- | :--- |
| **Declaración & Asignación** | `x = 10`<br/>`nombre = "Ana"` | `int x = 10;`<br/>`string nombre = "Ana";` | Python usa tipado dinámico; C++ requiere declaración explícita de tipos estáticos. |
| **Tipos Primitivos** | `int`, `float`, `bool`, `str` | `int`, `float`, `double`, `char`, `bool` | En C++ `float` vs `double` difieren en precisión/bytes. `char` usa comillas simples `'a'`. |
| **Operadores Aritméticos** | `+`, `-`, `*`, `/`, `//` (entera), `%`, `**` (potencia) | `+`, `-`, `*`, `/` (depende del tipo), `%`, `pow(b, e)` | En C++, `5 / 2` da `2` (división entera). Para decimal se requiere `5.0 / 2`. |
| **Operadores Lógicos** | `and`, `or`, `not` | `&&`, `\|\|`, `!` | Palabras clave en Python vs operadores simbólicos en C++. |

---

## Módulo 2: Entrada y Salida Estándar (I/O)

| Concepto Algorítmico | Implementación en Python | Implementación en C++ | Conceptos Clave & Diferencias |
| :--- | :--- | :--- | :--- |
| **Salida a Consola** | `print("Hola", valor)`<br/>`print(f"Total: {x}")` | `std::cout << "Hola " << valor << std::endl;` | `cout` usa operador de inserción `<<`. `endl` incluye salto de línea y flush. |
| **Entrada de Datos Simple** | `nombre = input("Nombre: ")`<br/>`edad = int(input())` | `std::string nombre;`<br/>`std::cin >> nombre;`<br/>`int edad; std::cin >> edad;` | `input()` siempre retorna `str` en Python (requiere `int()`). `cin >>` infiere por tipo pero se detiene en espacios. |
| **Lectura de Línea Completa** | `linea = input()` | `std::getline(std::cin, linea);` | En C++, si antes se usó `cin >>`, se requiere `cin.ignore()` para limpiar el `\n` residual del buffer. |

---

## Módulo 3: Estructuras Condicionales

| Concepto Algorítmico | Implementación en Python | Implementación en C++ | Conceptos Clave & Diferencias |
| :--- | :--- | :--- | :--- |
| **Condicional Simple** | `if condicion:`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`hacer_algo()` | `if (condicion) {`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`hacerAlgo();`<br/>`}` | Paréntesis obligatorios en la condición de C++; dos puntos `:` e indentación en Python. |
| **Condicional Doble** | `if c:`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`pass`<br/>`else:`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`pass` | `if (c) {`<br/>`}`<br/>`else {`<br/>`}` | Bloques delimitados por llaves `{}` en C++ vs indentación obligatoria en Python. |
| **Condicional Múltiple** | `if c1:`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`pass`<br/>`elif c2:`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`pass`<br/>`else:`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`pass` | `if (c1) {`<br/>`}`<br/>`else if (c2) {`<br/>`}`<br/>`else {`<br/>`}` | `elif` en Python vs `else if` en C++. |
| **Selección Múltiple** | `match opcion:` (Python 3.10+) | `switch (opcion) {`<br/>&nbsp;&nbsp;`case 1: ... break;`<br/>&nbsp;&nbsp;`default: ...`<br/>`}` | `switch` en C++ requiere `break;` para evitar *fall-through*. Solo aplica a enteros/char. |

---

## Módulo 4: Estructuras Repetitivas (Bucles)

| Concepto Algorítmico | Implementación en Python | Implementación en C++ | Conceptos Clave & Diferencias |
| :--- | :--- | :--- | :--- |
| **Bucle Mientras (`while`)** | `while condicion:`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`cuerpo` | `while (condicion) {`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`cuerpo;`<br/>`}` | La condición se evalúa antes de cada iteración. Riesgo de bucle infinito si no se actualiza la variable. |
| **Bucle Hacer-Mientras (`do-while`)** | Emulado con `while True:` y `if not cond: break` | `do {`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`cuerpo;`<br/>`} while (condicion);` | C++ garantiza al menos una ejecución obligatoria antes de evaluar la condición. |
| **Bucle Por Conteo (`for`)** | `for i in range(inicio, fin, paso):`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`print(i)` | `for (int i = inicio; i < fin; i += paso) {`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`cout << i;`<br/>`}` | `range(0, 5)` genera 0, 1, 2, 3, 4 (el límite superior `fin` nunca se incluye). |
| **Iteración sobre Colecciones** | `for item in lista:` | `for (const auto& item : lista) {` (C++11) | Bucle *for-each* / range-based for. |

---

## Módulo 5: Funciones y Modularidad

| Concepto Algorítmico | Implementación en Python | Implementación en C++ | Conceptos Clave & Diferencias |
| :--- | :--- | :--- | :--- |
| **Definición de Función** | `def sumar(a, b):`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`return a + b` | `int sumar(int a, int b) {`<br/>&nbsp;&nbsp;&nbsp;&nbsp;`return a + b;`<br/>`}` | C++ requiere tipo de retorno explícito (`void` si no retorna nada) y tipo de cada parámetro. |
| **Paso por Valor** | Objetos inmutables (`int`, `str`, `float`, `tuple`) se comportan por valor. | `void f(int x)`: recibe una copia independiente. | Modificar `x` dentro de la función no altera la variable original del llamador. |
| **Paso por Referencia** | Objetos mutables (`list`, `dict`) se pasan por referencia de objeto. | `void f(int& x)` o `void f(vector<int>& v)`: referencia directa con `&`. | En C++, el operador `&` en el parámetro permite modificar la variable original sin usar punteros. |
| **Ámbito de Variables (Scope)** | Variables locales al bloque de función; requiere `global` para reasignar globales. | Ámbito delimitado por llaves `{}`. Variables locales mueren al salir del bloque. | Visibilidad y ciclo de vida de variables. |

---

## Módulo 6: Arreglos y Estructuras de Datos Lineales

| Concepto Algorítmico | Implementación en Python | Implementación en C++ | Conceptos Clave & Diferencias |
| :--- | :--- | :--- | :--- |
| **Arreglo Estático (Tamaño fijo)** | No existe nativo estricto (se usan listas de tamaño `[0] * n`). | `int arr[5] = {1, 2, 3, 4, 5};` | En C++, el tamaño debe conocerse en compilación (salvo VLA no estándar). No verifica límites automáticamente. |
| **Arreglo Dinámico (Redimensionable)** | `mi_lista = []`<br/>`mi_lista.append(10)`<br/>`mi_lista.pop()` | `#include <vector>`<br/>`std::vector<int> v;`<br/>`v.push_back(10);`<br/>`v.pop_back();` | `list` en Python es internamente un array dinámico de punteros. `std::vector` en C++ almacena elementos contiguos en Heap. |
| **Acceso y Longitud** | `elem = lista[0]`<br/>`tam = len(lista)` | `int elem = v[0];`<br/>`size_t tam = v.size();` | Índices basados en 0 en ambos lenguajes. |
| **Matrices (2D)** | `matriz = [[1, 2], [3, 4]]`<br/>`matriz[fila][col]` | `int mat[2][2] = {{1, 2}, {3, 4}};`<br/>o `vector<vector<int>> mat;` | Acceso fila-columna `[i][j]`. |

---

## Módulo 7: Cadenas de Texto (Strings)

| Concepto Algorítmico | Implementación en Python | Implementación en C++ | Conceptos Clave & Diferencias |
| :--- | :--- | :--- | :--- |
| **Tipo de Dato** | `str` (inmutable) | `std::string` (mutable) o `char[]` estilo C | En Python no se puede hacer `s[0] = 'A'` (es inmutable); en C++ `std::string` sí lo permite. |
| **Longitud & Concatenación** | `len(s)`<br/>`s1 + s2` | `s.length()` o `s.size()`<br/>`s1 + s2` | Operaciones básicas equivalentes. |
| **Subcadenas / Slicing** | `s[inicio:fin]` | `s.substr(pos, count)` | En Python el segundo argumento es el índice fin; en C++ `substr` recibe la posición inicial y la *longitud*. |

---

## Módulo 8: Algoritmos Fundamentales

1. **Búsqueda Lineal:** Recorrer elemento a elemento hasta encontrar el objetivo o llegar al final ($O(N)$).
2. **Búsqueda Binaria:** Requiere arreglo ordenado; divide el espacio de búsqueda a la mitad en cada paso ($O(\log N)$).
3. **Ordenamiento Burbuja (Bubble Sort):** Comparar e intercambiar elementos adyacentes hasta que el arreglo esté ordenado ($O(N^2)$).
4. **Ordenamiento por Selección (Selection Sort):** Buscar el mínimo y colocarlo al inicio ($O(N^2)$).
5. **Recursividad Básica:** Caso base + caso recursivo (ej. Factorial, Fibonacci).
