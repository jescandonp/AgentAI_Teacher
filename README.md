# 🤖 AgentAI Teacher — Tutor Inteligente de Fundamentos de Programación

Sistema agéntico de tutoría personalizada para estudiantes universitarios de Fundamentos de Programación, con soporte dual para **Python** (Universidad EAN) y **C++** (Pontificia Universidad Javeriana).

---

## 🏛️ Arquitectura de 3 Capas

El proyecto opera bajo una arquitectura desacoplada y determinista para garantizar máxima confiabilidad pedagógica:

```text
AgentAI_Teacher/
├── directives/             # Capa 1: SOPs y Directivas Pedagógicas (Qué hacer)
│   ├── tutor_pedagogia_sop.md
│   ├── evaluacion_y_debug_sop.md
│   ├── diagramacion_y_modelos_sop.md
│   └── curriculum_fundamentos_matriz.md
│
├── execution/              # Capa 3: Herramientas Deterministas en Python (Hacer el trabajo)
│   ├── code_checker.py
│   ├── generate_trace_table.py
│   └── student_tracker.py
│
├── students/               # Espacios de Trabajo por Estudiante
│   ├── python_student/     # Nicolás Escandón (Universidad EAN)
│   └── cpp_student/        # Juan Coronado (Pontificia Universidad Javeriana)
│
├── resources/              # Material base, talleres y bases de conocimiento
│   ├── knowledge/          # Bases de conocimiento técnico y pedagógico para el agente
│   │   ├── cpp/            # C++ moderno, prevención de UB, gestión de memoria e inicialización
│   │   └── python/         # Modelo de datos Python, aliasing, SOLID y scaffolding
│   └── Students/           # Material de clase por estudiante
│       ├── Nicolas_Escandon/
│       └── Juan_Coronado/
│
├── .tmp/                   # Archivos temporales y persistencia de progreso
├── CLAUDE.md               # Sincronización de agentes de IA y aprendizajes continuos
├── AGENTS.md
└── GEMINI.md
```

---

## 🎯 Metodología Pedagógica

- **Modelo E-P-S (Entradas - Procesos - Salidas):** Análisis previo y estructuración algorítmica obligatoria antes del código.
- **Tutoría Socrática y Pistas en 4 Niveles:** Guía progresiva (Pregunta guía $\rightarrow$ Traza/Señalización $\rightarrow$ Ejemplo análogo $\rightarrow$ Corrección comentada) sin dar soluciones directas.
- **Diagramación Visual (Mermaid):** Diagramas de flujo y modelos mentales de memoria (Stack/Heap vs. referencias de objetos).
- **Traducción Guiada:** De pseudocódigo a Python (EAN) y de bloques Lego a sintaxis estricta C++ (Javeriana).

---

## 🛠️ Herramientas de Ejecución (Capa 3)

1. **Validador Estático de Código (`code_checker.py`):**
   ```bash
   python execution/code_checker.py --lang python --file ruta/al/archivo.py
   python execution/code_checker.py --lang cpp --file ruta/al/archivo.cpp
   ```

2. **Generador de Trazas y Diagramas (`generate_trace_table.py`):**
   ```bash
   python execution/generate_trace_table.py --type trace --vars "i,contador,total" --steps 4
   python execution/generate_trace_table.py --type flowchart --template while_loop
   ```

3. **Gestor de Progreso de Estudiantes (`student_tracker.py`):**
   ```bash
   python execution/student_tracker.py --summary
   python execution/student_tracker.py --student python_student --update-topic "Funciones y Modularidad" --status "Dominado"
   ```

---

## 👥 Estudiantes Activos

- **Nicolás Escandón:** Algoritmos y Programación - Fundamentos (Universidad EAN). Enfoque en Python, funciones, listas y menús interactivos.
- **Juan Coronado:** Solución Problemas de Programación (Pontificia Universidad Javeriana). Enfoque en C++, diagramación formal y estructuras de control.
