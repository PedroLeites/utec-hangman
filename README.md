## utec-hangman
# Juego del Ahorcado

## 1. Descripción del proyecto

Es una implementación del clásico juego del ahorcado desarrollada en Python. El objetivo es que el jugador descubra una palabra o título seleccionado aleatoriamente de una lista, ingresando letras a través de la terminal.

El jugador dispone de un máximo de **6 intentos incorrectos** para adivinar todas las letras de la palabra. En cada turno, el programa informa si la letra ingresada es correcta o incorrecta y actualiza el progreso de la partida.

El proyecto utiliza programación modular y orientación a objetos para organizar el código y separar las responsabilidades de cada componente.

## 2. Estructura del proyecto

El proyecto está organizado de la siguiente manera:

```text
hangman_project/
│
├── main.py
├── game.py
├── utils.py
├── wordlist.txt
└── README.md
```

### `main.py`

Es el punto de entrada de la aplicación. Se encarga de iniciar la partida, interactuar con el jugador y controlar el flujo de ejecución.

Sus principales responsabilidades son:

- Obtener una palabra aleatoria.
- Crear una instancia de `HangmanGame`.
- Mostrar el estado inicial de la partida.
- Solicitar letras al jugador.
- Validar las entradas.
- Evitar que se ingresen letras repetidas.
- Informar si las letras ingresadas son correctas o incorrectas.
- Actualizar y mostrar el progreso del juego.
- Comprobar las condiciones de victoria y derrota.

### `game.py`

Contiene la clase `HangmanGame`, encargada de representar y administrar el estado de una partida.

**Atributos principales:**

| Atributo | Descripción |
|---|---|
| `word` | Palabra que el jugador debe adivinar. |
| `guessed_letters` | Lista de letras que fueron adivinadas correctamente. |
| `incorrect_letters` | Lista de letras ingresadas que no pertenecen a la palabra. |
| `max_errors` | Cantidad máxima de errores permitidos (6). |
| `errors` | Cantidad de errores cometidos durante la partida. |

**Métodos principales:**

| Método | Descripción |
|---|---|
| `__init__(word)` | Inicializa una partida y sus atributos. |
| `display_progress()` | Muestra las letras adivinadas y oculta las restantes. Los espacios, números y signos se muestran automáticamente. |
| `process_guess(letter)` | Procesa una letra, la registra en la lista correspondiente y actualiza los errores cuando corresponde. |
| `is_won()` | Comprueba si se adivinaron todas las letras de la palabra. |
| `is_lost()` | Comprueba si se alcanzó el máximo de errores permitidos. |
| `display_hangman()` | Muestra el gráfico ASCII del ahorcado según la cantidad de errores. |

### `utils.py`

Contiene funciones auxiliares utilizadas por el programa.

**Función principal:**

- `get_random_word()`: lee el archivo `wordlist.txt`, obtiene las palabras disponibles y selecciona una aleatoriamente para iniciar la partida.

### `wordlist.txt`

Es el archivo de texto que contiene las palabras y los títulos disponibles para el juego.

Cada entrada debe escribirse en una línea diferente. Se pueden incluir palabras, frases y títulos con espacios, números o signos de puntuación.

Ejemplo:

```text
the matrix
spider-man: no way home
wall-e
r2-d2: beneath the dome
breaking bad
```

Los caracteres que no son letras se muestran automáticamente y no necesitan ser adivinados.

## 3. Flujo de ejecución

El funcionamiento general del programa sigue estos pasos:

1. **Inicio:** se ejecuta `main.py` y se muestra el mensaje de bienvenida.
2. **Selección de palabra:** se llama a `get_random_word()`, que obtiene una palabra aleatoria desde `wordlist.txt`.
3. **Inicialización:** se crea un objeto de la clase `HangmanGame` con la palabra seleccionada.
4. **Presentación del estado:** se muestra el gráfico ASCII, el progreso de la palabra, las letras ingresadas y los intentos restantes.
5. **Ingreso de una letra:** el jugador ingresa una letra a través de la terminal.
6. **Validación:** se comprueba que la entrada contenga una sola letra y que no haya sido ingresada anteriormente.
7. **Procesamiento:** se llama a `process_guess()` para determinar si la letra pertenece a la palabra.
   - Si es correcta, se agrega a `guessed_letters`.
   - Si es incorrecta, se agrega a `incorrect_letters` y se incrementa el contador de errores.
8. **Actualización:** se muestra nuevamente el progreso de la palabra, las listas de letras y el gráfico ASCII.
9. **Finalización:** se comprueba si el jugador ganó o perdió.
   - Si adivinó todas las letras, se muestra un mensaje de victoria.
   - Si alcanzó los seis errores, se muestra un mensaje de derrota y se revela la palabra.
10. **Fin:** termina la ejecución de la partida.

## 4. Cómo ejecutar el proyecto

### Requisitos

- Python 3 instalado.
- Una terminal o consola de comandos.
- Los archivos del proyecto disponibles localmente.

El proyecto utiliza exclusivamente módulos de la biblioteca estándar de Python, por lo que no requiere instalar dependencias externas.

### Pasos para ejecutar

1. Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

2. Ingresar a la carpeta del proyecto:

```bash
cd utec-hangman/hangman_project
```

3. Ejecutar la aplicación:

```bash
python3 main.py
```

## 5. Reglas del juego

- El programa selecciona una palabra aleatoria de `wordlist.txt`.
- El jugador debe ingresar una letra por turno.
- Solo se aceptan entradas de una única letra.
- No se permiten letras repetidas, tanto correctas como incorrectas.
- Las letras acertadas se muestran en sus posiciones correspondientes.
- Las letras incorrectas se registran y se muestran al jugador.
- Los espacios, números y signos de puntuación se revelan automáticamente.
- Cada letra incorrecta incrementa el contador de errores.
- El jugador dispone de un máximo de seis errores.
- La partida finaliza cuando se adivinan todas las letras o se alcanza el máximo de errores.

---

**Proyecto desarrollado como parte de las actividades del Certificado en Desarrollo de Soluciones Digitales con IA de UTEC.**
