## Atributos y propiedades

Para cambiar los atributos dentro de un objeto, tu clase necesitará algunas **propiedades**.

Las propiedades son unos métodos especiales que permiten **obtener** o **establecer** el valor de un atributo, y son referidos como **getter** y **setter**.

### Getters y setters

Para esta sección, puedes ver el vídeo de abajo, o seguir las instrucciones escritas.

<video width="768" height="576" controls>
<source src="resources/clip3.mp4" type="video/mp4">
Tu navegador no soporta la etiqueta de vídeo, prueba FireFox o Chrome
</video>

Es posible acceder a los atributos de un objeto directamente. Por ejemplo, podrías añadir el siguiente código en la parte inferior de tu programa para cambiar el atributo `palo` de `mi_carta` y luego mostrar el objeto:

```python
mi_carta.palo = "trebol"
print(mi_carta)
```

Sin embargo, acceder directamente a los atributos no es una buena idea, porque las personas podrían hacer cosas como esta:

```python
mi_carta.palo = "dinosaurios"
print(mi_carta)
```

En su lugar, vamos a crear propiedades para tu clase: un **getter** y un **setter** para acceder al atributo `palo`.

+ Antes de empezar, vuelve a tu método `__init__` y localiza `self.palo`. Añade un guión bajo `_` antes de `palo` para indicar que no quieres que las personas accedan directamente a este atributo.

```python
def __init__(self, palo, numero):
    self._palo = palo
```

--- collapse ---
---
title: ¿El guión bajo significa que el atributo no se puede cambiar directamente?
---

Añadir un guión bajo es una buena práctica y un buen estilo de programación.

Sin embargo, el guión bajo **no impedirá** a las personas cambiar el atributo directamente — es una convención que indica que ellos **no deberían**. Si quieres probar esto, añade un guión bajo a tu código para cambiar el atributo a `"dinosaurios"`:

```python
mi_carta._palo = "dinosaurios"
```

Verás que todavía puedes cambiar el atributo así como antes.

--- /collapse ---

#### Creando un getter

+ Vuelve a la definición de la clase `Carta`, añade un nuevo método llamado `palo`, y haz que devuelva el valor del atributo `_palo`.

```python
def palo(self):
    return self._palo
```

+ Añade un **decorador** a este método para decir que es una propiedad.

```python
@property
def palo(self):
    return self._palo
```

Ahora, cada vez que alguien usa el valor `mi_carta.palo` en su programa, este getter será llamado y el usuario recibirá el valor de `self._palo` almacenado en el objeto `mi_carta`.

--- collapse ---
---
title: ¿Qué es un decorador?
---

En la programación orientada a objetos, los decoradores te permiten añadir comportamientos adicionales (o funcionalidades) a una clase.

Un decorador puede ser pensado como una envoltura a un método: contiene el método pero también amplía su funcionalidad.

El decorador `@property` en Python necesita ser añadido al método getter para definir el método como una propiedad.

--- /collapse ---

#### Creando un setter

+ Añade otro método. Es importante que este método **también se llame `palo`**. Debería tomar un dato que represente el nuevo palo que el usuario desea establecer, y hacer una comprobación básica para asegurarse de que ese dato sea uno de los palos habituales disponibles en una baraja de cartas.

```python
def palo(self, palo):
    if palo in ["corazones", "trebol", "diamantes", "espadas"]:
        self._palo = palo
    else:
        print("¡Esto no es un palo!")
```
+ Ahora añade un decorador a este método para decir que es el setter para `palo`.

```Python
@palo.setter
def palo(self, palo):
```

Como en el método getter, este decorador define el método como una propiedad. Ahora, cada vez que alguien intente establecer el atributo `palo` (por ejemplo, escribiendo `mi_carta.palo = "espadas"`), se llamará a la propiedad `@palo.setter`. En este ejemplo, el valor `"espadas"` se le pasará como parámetro `palo`.

Ten en cuenta que usando propiedades de getter y setter; y decoradores, puedes tener dos funciones con el mismo nombre, una que se llama cuando se obtiene el valor, y otra que se llama cuando se establece el valor.

--- collapse ---
---
title: ¿Por qué usamos propiedades?
---

¿Por qué queremos utilizar los decoradores `@property` y `.setter` para crear propiedades en lugar de crear un método `get_palo()` y un método `set_palo()`?

Hay varias razones:

- Es más corto y atractivo poder referirse a `carta.palo` en lugar de `carta.get_palo()` y `carta.set_palo()`. Por ejemplo:

```python
mi_palo = carta.palo
carta.palo = "espadas"
```

es mucho más fácil que:

```python
mi_palo = carta.get_palo()
carta.set_palo("espadas")
```

- Puedes hacer que funciones complejas se vean como simples operaciones. Piensa en el ejemplo de LED en el paso 1: no necesitas conocer los detalles de cómo encender un LED con tu computadora – `on()` lo hace todo por ti.

- Si utilizas propiedades en lugar de permitir el acceso directo a los atributos y necesitas cambiar cómo funciona la clase puedes hacerlo sin romper ningún código que use la clase. Por ejemplo, el setter original de `palo` que escribiste simplemente almacenó el palo, pero digamos que quieres guardarlo en letras mayúsculas. Para ello, puedes simplemente cambiar el código dentro de la propiedad:

```python
@palo.setter
def palo(self, palo):
        if palo in ["corazones", "trebol", "diamantes", "espadas"]:
            self._palo = palo.upper()
        else:
            print("¡Esto no es un palo!")
```

Ahora todos los palos se almacenarán como mayúsculas, mientras que cualquier código que utilice la propiedad `palo` seguirá funcionando.

Si dejas que la gente acceda directamente al atributo `palo`, no podrás cambiar ningún aspecto del código más adelante.

--- /collapse ---

+ Ejecuta el programa. Si ahora intentas cambiar el palo de la carta a cualquier otra cosa que no sea uno de los palos de la lista, deberías ver aparecer `"¡Esto no es un palo!`, y el palo no debe cambiar.

Ten en cuenta que actualmente no tienes ninguna validación en el método `__init__`, así que aún puedes crear el 2 de Dinosaurios de esta manera:

```Python
otra_carta = Carta("Dinosaurios", "2")
```
