# Propuesta Pedagógica de Refuerzo en C++ (Juan Diego Coronado)
**Pontificia Universidad Javeriana — Fundamentos de Programación**  
**Fecha:** 28 de Septiembre, 2026  
**Enfoque:** Modelo E-P-S (Entradas-Procesos-Salidas), Bloques Lego, Arreglos Unidimensionales, Funciones y Prevención de Comportamientos Indefinidos (*Out-of-Bounds*).

---

## 🎯 Objetivos Pedagógicos del Bloque de Refuerzo
1. **Consolidación de Arreglos y Límites Seguros:** Reforzar la indexación base cero `0` hasta `TAM - 1` para erradicar errores de tipo *off-by-one* (evitar accesos fuera de rango `i <= TAM`).
2. **Modularización Limpia (Funciones):** Afianzar la declaración de prototipos y el paso de arreglos por referencia implícita (`int v[]`, `int tamanio`).
3. **Patrones Algorítmicos Fundamentales:**
   - Acumulación y cálculo de promedios.
   - Búsqueda secuencial (*Linear Search*).
   - Detección de extremos (Mínimos y Máximos).
   - Arreglos paralelos para modelar entidades del mundo real.

---

## 📋 Resumen de la Progresión de Complejidad

| Nivel | Ejercicio | Conceptos Integrados | Tiempo Estimado |
| :--- | :--- | :--- | :--- |
| **1. Baja** | **Monitoreo de Sensores Térmicos** | Arreglos fijos, acumuladores, bucles `for`, condicionales `if/else`, límites de índices seguros. | 20 - 30 min |
| **2. Media** | **Gestor de Calificaciones y Búsqueda Modular** | Prototipos de función, paso de arreglos, búsqueda lineal (`buscarNota`), cálculo de valor máximo (`obtenerMayor`). | 35 - 45 min |
| **3. Alta** | **Sistema de Caja y Ventas con Arreglos Paralelos** | Menú interactivo (`while`/`switch`), arreglos paralelos (`precios[]`, `cantidades[]`), funciones modulares, descuentos escalonados e IVA. | 50 - 65 min |

---

## 🧩 Detalle de los Ejercicios

### 🟢 Ejercicio 1: Complejidad Baja — *Monitoreo de Sensores Térmicos*
> **Contexto:** En una estación meteorológica se tienen `TAM = 8` sensores de temperatura (en °C).

**Requisitos del Programa:**
1. **Entradas (E):**
   - Declarar una constante global `const int TAM = 8;`.
   - Inicializar un arreglo `double temperaturas[TAM] = {0};`.
   - Solicitar al usuario que ingrese la temperatura registrada por cada uno de los 8 sensores mediante un bucle `for`.
2. **Procesos (P):**
   - Calcular la temperatura **promedio** de la estación (usando un acumulador `suma`).
   - Contar cuántos sensores registraron temperaturas **críticas** (temperatura $\ge 35.0$ °C).
   - Contar cuántos sensores registraron temperaturas **bajas** (temperatura $< 15.0$ °C).
3. **Salidas (S):**
   - Imprimir la lista de todas las temperaturas ingresadas con su índice correspondiente: `[Sensor i]: X °C`.
   - Mostrar el promedio general con formato claro.
   - Reportar el conteo de temperaturas críticas y bajas.

**Puntos Clave a Reforzar:**
- ✅ Control estricto de índices: el bucle debe iterar estrictamente en `i = 0; i < TAM; i++`.
- ✅ Inicialización explícita del acumulador `double suma = 0.0;`.

---

### 🟡 Ejercicio 2: Complejidad Media — *Gestor de Rendimiento Académico Modular*
> **Contexto:** Un profesor necesita analizar las notas finales (escala 0.0 a 5.0) de un curso de `TAM = 10` estudiantes usando funciones modulares.

**Requisitos del Programa:**
1. **Estructura Modular (Funciones requeridas):**
   - `void ingresarNotas(double notas[], int cant);`  
     *(Pide al usuario las notas y valida que cada nota esté en el rango de $0.0$ a $5.0$).*
   - `void mostrarNotas(const double notas[], int cant);`  
     *(Imprime las notas en pantalla).*
   - `double calcularPromedio(const double notas[], int cant);`  
     *(Retorna el promedio del curso).*
   - `int buscarNota(const double notas[], int cant, double valorBuscado);`  
     *(Retorna el índice de la primera ocurrencia de la nota o `-1` si no existe).*
   - `int obtenerIndiceMejorNota(const double notas[], int cant);`  
     *(Retorna la posición/índice del estudiante con la nota más alta).*

2. **Flujo del `main()`:**
   - Declarar arreglo `double notas[TAM];`.
   - Invocar `ingresarNotas` y `mostrarNotas`.
   - Mostrar el promedio y la nota más alta (junto con el número de estudiante / índice).
   - Pedir al usuario una nota para buscar y notificar si se encontró o no en el curso.

**Puntos Clave a Reforzar:**
- ✅ Separación en prototipos (`header`) e implementaciones al final del archivo.
- ✅ Patrón de búsqueda con bandera o retorno inmediato `-1`.
- ✅ Algoritmo clásico de búsqueda de máximo (`double maximo = notas[0]; int indiceMax = 0;`).

---

### 🔴 Ejercicio 3: Complejidad Alta — *Terminal de Facturación con Arreglos Paralelos*
> **Contexto:** Una tienda de suministros tecnológicos maneja un catálogo de `MAX_PROD = 5` productos. Se desea crear un sistema de facturación y control de inventario utilizando arreglos paralelos y un menú interactivo.

**Estructura de Datos (Arreglos Paralelos):**
- `int codigos[MAX_PROD] = {101, 102, 103, 104, 105};`
- `double precios[MAX_PROD] = {15000.0, 45000.0, 80000.0, 120000.0, 25000.0};`
- `int stock[MAX_PROD] = {10, 8, 5, 3, 12};`
- `int compras[MAX_PROD] = {0};` *(Registra las unidades que el cliente lleva de cada producto)*.

**Requisitos del Programa:**
1. **Menú Interactivo (`while` + `switch`):**
   - `1. Mostrar Catálogo y Stock Disponible.`
   - `2. Agregar Producto al Carrito (por código y cantidad solicitada).`
   - `3. Ver Resumen del Carrito actual.`
   - `4. Finalizar Compra y Facturar.`
   - `5. Salir sin comprar.`
2. **Validaciones y Lógica de Negocio:**
   - **Validación de Stock:** No permitir comprar más unidades de las disponibles en `stock[]`.
   - **Búsqueda por Código:** Usar una función `int buscarProductoPorCodigo(const int codigos[], int cant, int codigoBuscado);`.
   - **Cálculo de Factura (E-P-S):**
     - Subtotal = $\sum (\text{precios}[i] \times \text{compras}[i])$.
     - Si el subtotal supera $\$150.000$ $\rightarrow$ **Descuento del 10%**.
     - Si el subtotal está entre $\$70.000$ y $\$150.000$ $\rightarrow$ **Descuento del 5%**.
     - IVA del 19% aplicado al subtotal con descuento.
     - Total a pagar = $(\text{Subtotal} - \text{Descuento}) + \text{IVA}$.
   - **Producto Estrella:** Al facturar, indicar cuál fue el producto del que más unidades compró el cliente.

**Puntos Clave a Reforzar:**
- ✅ Coordinación de arreglos paralelos a través del mismo índice `i`.
- ✅ Actualización de estados (reducir `stock[i]` al comprar).
- ✅ Integración total: bucle interactivo, condicionales compuestos, funciones, acumuladores y salidas con formato comercial.
