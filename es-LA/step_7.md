## Una baraja de cartas

Ahora que tienes un modelo básico de una carta, es hora de crear un mazo.

+ Crea una clase `Baraja`. Puedes hacer esto en el mismo archivo donde escribiste tu clase `Carta`, o en uno separado. Si lo haces en un archivo diferente (por ejemplo, `deck.py`), tendrás que importar la clase `Carta` en la parte superior de ese archivo con este código:

```python
from card import Carta
```

En esta línea de código, `card` es el nombre del archivo Python que contiene la clase, menos la extensión `.py`, y `Carta` es el nombre de la clase.

+ Crea una nueva clase `Baraja` e incluye un método `__init__` en él. Esta vez no necesitaremos ningún parámetro que no sea `self`, que es obligatorio.

```python
class Baraja:

    def __init__(self):
```

+ La `Baraja` tendrá que almacenar una lista de cartas, cada una de las cuales será un objeto `Carta`. Añade un atributo llamado `_cartas` al método `__init__`, y defínelo como una lista vacía por ahora.

```python
class Baraja:

    def __init__(self):
        self._cartas = []
```

+ Ahora vamos a escribir un método para llenar la baraja con las 52 cartas necesarias. Comienza creando un método llamado `completar`:

```Python
def completar(self):
```

+ Dentro del método, define dos listas. Una debe contener todos los palos posibles de la carta, y la otra todos los números posibles de la carta, como cadenas:

```Python
def completar(self):
    palos = ["corazones", "trebol", "diamantes", "espadas"]
    numeros = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
```

--- collapse ---
---
title: ¿Existe una manera más eficiente de hacer una lista de números?
---

¡Sí! En lugar de escribirlos todos, puedes usar **comprensión de lista**, que es una forma rápida de crear una nueva lista basada en una lista existente.

Así que, para crear una lista que contenga los números de 2 a 10 como cadenas, puedes usar el código:

```Python
numeros = [str(n) for n in range(2,11)]
```

Esto significa:
- Dame `str(n)` (la versión string de n)
- Por cada `n in range(2, 11)` (recuerda que la función `range()` comenzará en 2 y se detendrá en (pero no incluirá) 11)

Luego añade una lista que contenga las cartas de imagen y el as al final:

```Python
numeros = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
```

--- /collapse ---

+ Para que `completar` genere la baraja de cartas, solo tenemos que combinar objetos de las dos listas — para cada palo, para cada número, crear un objeto `Carta`. Una forma de hacer esto es con bucles anidados:

```Python
cartas = []                         # Crea una lista vacía de cartas
for palo in palos:                  # Por cada palo...
    for numero in numeros:          # Por cada número...
        # Crea un nuevo objeto Carta y añádelo a la lista
        cartas.append( Carta(palo, numero) )  
self._cartas = cartas                 # Luego señale self._cartas a esta lista
```

Sin embargo, el uso de bucles anidados puede hacer que el código sea más complicado. Para simplificar el código, puedes utilizar una **comprensión de lista**:

```Python
self._cartas = [ Carta(p, n) for p in palos for n in numeros ]
```

Este código significa:
- Establecer `self._cartas` a
- `[ una lista ]`
- de objetos `Carta`
- que contiene cada combinación de `p, n`, haciendo un bucle a través de `for p in palos` y `for n in numeros`

Si deseas obtener más información sobre las comprensiones de listas, echa un vistazo a la siguiente información.

[[[generic-python-simple-list-comprehensions]]]

+ Vamos a probar si tu método construye correctamente una baraja. Vuelve a tu método `__init__`, llama al método `completar()`, luego imprime la lista de cartas:

```Python
def __init__(self):
    self._cartas = []
    self.completar()
    print(self._cartas)
```

+ Crea una instancia de la clase `Baraja` para comprobar si estás obteniendo la baraja que deseas.

--- hints ---

--- hint ---

Crea una instancia de una clase declarando una variable y haciéndola igual a `Clase()`.

--- /hint ---

--- hint ---

Revisa cómo instanciaste un objeto de la clase `Carta`.

--- /hint ---

--- hint ---

Usa este código:

```Python
mi_baraja = Baraja()
```

--- /hint ---

--- /hints ---

Deberías ver el siguiente resultado:

```Python
[2 de corazones, 3 de corazones, 4 de corazones, 5 de corazones, 6 de corazones, 7 de corazones, 8 de corazones, 9 de corazones, 10 de corazones, J de corazones, Q de corazones, K de corazones, A de corazones, 2 de trebol, 3 de trebol, 4 de trebol, 5 de trebol, 6 de trebol, 7 de trebol, 8 de trebol, 9 de trebol, 10 de trebol, J de trebol, Q de trebol, K de trebol, A de trebol, 2 de diamantes, 3 de diamantes, 4 de diamantes, 5 de diamantes, 6 de diamantes, 7 de diamantes, 8 de diamantes, 9 de diamantes, 10 de diamantes, J de diamantes, Q de diamantes, K de diamantes, A de diamantes, 2 de espadas, 3 de espadas, 4 de espadas, 5 de espadas, 6 de espadas, 7 de espadas, 8 de espadas, 9 de espadas, 10 de espadas, J de espadas, Q de espadas, K de espadas, A de espadas]
```
