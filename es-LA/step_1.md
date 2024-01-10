## Introducción

Crea un modelo de un mazo de cartas que forme la base para construir programas de juegos de cartas digitales como Poker o Rummy.

### Lo que harás

Aprenderás a utilizar el paradigma de programación orientado a objetos en Python para crear un modelo reutilizable de un mazo de cartas.

La programación orientada a objetos (POO) es una forma de organizar tu código para que sea más fácil de entender, reutilizar y cambiar. POO te permite combinar datos (variables) y funcionalidades, y empaquetarlos juntos dentro de **objetos**.

![Cartas](images/cards.jpg)

_Imagen de Rosapicci (Trabajo propio) [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), a través de Wikimedia Commons_

--- collapse ---
---
title: ¿Qué es la Programación Orientada a Objetos?
---

Seguramente has escuchado sobre la programación orientada a objetos, pero tal vez no estés seguro de qué es. Tal vez incluso hayas intentado leer guías o libros, pero te perdiste en la jerga.

La programación orientada a objetos es parte integral de muchos lenguajes de programación, y es simplemente un estilo diferente de programación.

#### ¿Qué es un objeto?

Los objetos se utilizan para modelar cosas en código. Un objeto puede representar un elemento físico, como un LED, o puede representar una unidad digital, tal como una cuenta bancaria o un personaje en un juego de computadora. Un objeto es básicamente un grupo de datos y funciones. Dado que puedes definir tus propios objetos, ¡puedes representar cualquier cosa que desees con un objeto!

#### ¿Dónde habría visto objetos antes?

Veamos un ejemplo de un LED conectado a una computadora Raspberry Pi. No te preocupes si nunca has conectado un LED o has hecho otra informática física — ¡lo importante aquí es el código!

![led conectado al pin 17](images/LED-GP17.gif)

A la izquierda del diagrama están los pines GPIO de la Raspberry Pi, los que nos permiten controlar los componentes que están conectados a ellos. El LED está conectado al pin 17. Para encender el LED, utilizarías el siguiente código de Python:

```python
from gpiozero import LED
rojo = LED(17)           
rojo.on()
```

Para interactuar con el LED, hemos creado un objeto `LED` que representa el LED físico en código. Tiene el nombre `rojo` de manera que nos podamos referir a ese objeto LED específico.

```python
rojo = LED(17)
```

Podemos conectar otro LED al pin 21, y luego crear otro objeto con un nombre diferente para representarlo:

```python
verde = LED(21)
```

#### ¿Por qué querría usar objetos?

En nuestro ejemplo, creamos un objeto `LED` para modelar un LED físico en código. También incluimos un comando para controlar el LED, en este caso para encenderlo con `on`. Estos comandos se denominan métodos — funciones personalizadas específicamente diseñadas para interactuar con un objeto.

Una de las ventajas del uso de la programación orientada a objetos es que se pueden omitir detalles innecesarios cuando utilizamos un método. No necesitamos saber exactamente cómo funciona un método para poder utilizarlo, simplemente podemos llamarlo para lograr el resultado deseado. En nuestro ejemplo, no necesitamos saber nada sobre el método `on()` aparte del hecho de que usarlo en nuestro objeto `LED` hará que el LED físico se encienda.

--- /collapse ---

### Lo que aprenderás

Este proyecto incluye elementos de los siguientes aspectos del [currículo de creación digital de Raspberry Pi](http://rpf.io/curriculum){:target="_blank"}:

+ [Aplicar técnicas complejas de programación para resolver problemas del mundo real](https://curriculum.raspberrypi.org/programming/maker/){:target="_blank"}

### Información adicional para educadores

Si necesitas imprimir este proyecto, usa la [versión para imprimir](https://projects.raspberrypi.org/en/projects/deck-of-cards/print){:target="_blank"}.

Utiliza el link que aparece en el pie de página para acceder al repositorio de GitHub de este proyecto que contiene todos los recursos (incluyendo un ejemplo de un proyecto terminado) en la carpeta 'en/resources'.
