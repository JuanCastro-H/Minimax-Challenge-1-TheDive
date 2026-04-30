# 🐱🐭 Juego del Gato y el Ratón

Un juego de estrategia por turnos donde un ratón debe escapar a su cueva mientras es perseguido por un gato inteligente. El proyecto implementa inteligencia artificial usando el algoritmo **Minimax** para crear oponentes desafiantes.

## 🎮 Descripción del Juego

El ratón debe llegar a su cueva antes de ser capturado por el gato. El juego se desarrolla en un tablero rectangular con bordes que actúan como muros infranqueables.

### Reglas Básicas
- **🐭 Ratón (Objetivo)**: Llegar a la cueva 🏠
- **🐱 Gato (Obstáculo)**: Capturar al ratón antes de que escape
- **Movimientos**: 8 direcciones (incluye diagonales)
- **Victoria del Ratón**: Alcanzar la cueva
- **Victoria del Gato**: Capturar al ratón (ocupar la misma casilla)

## 🚀 Características

### Modos de Juego
1. **Bot vs Bot**: Ambos jugadores controlados por IA
2. **Jugador vs Aleatorio**: Controlas al ratón, el gato se mueve aleatoriamente
3. **Jugador vs IA**: Controlas al ratón, el gato usa inteligencia artificial
4. **Simulación Aleatoria**: Ambos jugadores se mueven aleatoriamente

### Inteligencia Artificial
- **Algoritmo Minimax**: El gato y ratón pueden usar estrategias óptimas
- **Evaluación heurística**: Calcula distancias y posiciones estratégicas
- **Profundidad configurable**: Control del nivel de dificultad

### Configuraciones
- **Tablero personalizable**: Mínimo 10x10 casillas
- **Posiciones iniciales**:
  - Ratón en esquina, gato en el centro
  - Esquinas opuestas
  - Posiciones completamente aleatorias

## 🛠️ Instalación y Ejecución

### Requisitos
- Python 3.6 o superior
- Librerías estándar (incluidas): `random`, `os`, `time`

### Ejecución
```bash
python juego_gato_raton.py
```

## 🎯 Controles

### Movimientos del Jugador Manual
- **W**: Arriba
- **S**: Abajo  
- **A**: Izquierda
- **D**: Derecha
- **Q**: Diagonal arriba-izquierda
- **E**: Diagonal arriba-derecha
- **Z**: Diagonal abajo-izquierda
- **C**: Diagonal abajo-derecha

## 🧠 Algoritmo Minimax

El proyecto implementa el algoritmo Minimax para crear una IA competitiva:

### Funcionamiento
1. **Evaluación**: Calcula qué tan favorable es una posición
2. **Simulación**: Explora movimientos futuros (árbol de decisiones)
3. **Optimización**: 
   - Ratón busca maximizar su puntuación
   - Gato busca minimizar la puntuación del ratón

### Función de Evaluación
```
valor = distancia_gato_al_ratón - distancia_ratón_a_cueva
```
- **Valores altos**: Favorable para el ratón
- **Valores bajos**: Favorable para el gato

## 📁 Estructura del Código

### Funciones Principales
- `limpiar_la_consola()`: Mejora la presentación visual
- `nuevo_movimiento()`: Genera movimientos aleatorios válidos
- `evaluar_estado_simple()`: Función heurística para Minimax
- `minimax_simple()`: Implementación del algoritmo Minimax
- `mover_jugador_ia()`: Interfaz entre IA y juego
- `jugador_manual()`: Manejo de input del usuario
- `imprimir_tablero()`: Visualización del estado del juego

### Modos de Juego
- `prueba_con_ia()`: Ambos jugadores con IA
- `prueba_compleja()`: Movimientos completamente aleatorios
- `prueba_compleja_manual()`: Jugador vs aleatorio
- `prueba_compleja_manual_con_bot()`: Jugador vs IA

## 🎨 Interfaz

### Símbolos del Tablero
- `🐭`: Ratón (jugador principal)
- `🐱`: Gato (perseguidor)
- `🏠`: Cueva (objetivo del ratón)
- `#`: Muros/bordes
- `.`: Espacios vacíos

### Ejemplo Visual
```
# # # # # # # # # #
# 🐭 . . . . . . . #
# . . . . . . . . #
# . . . 🐱 . . . . #
# . . . . . . . 🏠 #
# # # # # # # # # #
```

## ⚙️ Personalización

### Cambiar Dificultad de IA
Modifica el parámetro `profundidad` en las llamadas a `minimax_simple()`:
- `profundidad = 1`: IA básica
- `profundidad = 2`: IA moderada (por defecto)
- `profundidad = 3+`: IA avanzada (más lenta)

### Activar Diferentes Modos
En la sección final del código, descomenta la función deseada:
```python
# Descomenta una de estas líneas:
# prueba_con_ia(tablero, posicion_raton, posicion_gato, cueva, diccionario_movimientos)
# prueba_compleja_manual(tablero, posicion_raton, posicion_gato, cueva)
# prueba_compleja(tablero, posicion_raton, posicion_gato, cueva)
prueba_compleja_manual_con_bot(tablero, posicion_raton, posicion_gato, cueva)
```

## 🧪 Aspectos Técnicos

### Algoritmo de IA
- **Tipo**: Minimax con poda implícita
- **Complejidad temporal**: O(b^d) donde b=movimientos posibles, d=profundidad
- **Estrategia**: Búsqueda en árbol de juego con evaluación heurística

### Validaciones
- Movimientos dentro de los límites del tablero
- Prevención de colisiones con muros
- Verificación de reglas específicas por jugador

### Optimizaciones
- Limpieza de consola para mejor experiencia visual
- Pausas temporales para seguimiento de movimientos
- Manejo de casos extremos (sin movimientos válidos)

## 🎓 Propósitos Educativos

Este proyecto es ideal para aprender:
- **Algoritmos de IA**: Implementación práctica de Minimax
- **Programación orientada a funciones**: Código modular y reutilizable
- **Lógica de juegos**: Manejo de estados, turnos y condiciones de victoria
- **Interacción usuario-programa**: Input validation y experiencia de usuario

## 🔄 Posibles Mejoras

- Implementar poda Alpha-Beta para optimizar Minimax
- Agregar múltiples niveles de dificultad
- Incluir obstáculos internos en el tablero
- Sistema de puntuaciones y estadísticas
- Interfaz gráfica con pygame o tkinter
- Modos multijugador en red

---

**Autor**: JUAN MANUEL CASTRO HERNANDEZ