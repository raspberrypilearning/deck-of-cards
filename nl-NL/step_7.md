## Een spel kaarten

Nu je een basismodel van een kaart hebt, is het tijd om een kaartspel te maken.

+ Maak een class `Spel`. Je kunt dit doen in hetzelfde bestand waar je je `Kaart` class hebt geschreven, of in een andere. Als je het in een ander bestand doet (bijvoorbeeld `deck.py`), moet je de class `Kaart` bovenaan dat bestand importeren met deze code:

```python
from card import Kaart
```

In deze coderegel is `card` de naam van het Python-bestand dat de klasse bevat, minus de extensie `.py`, en `Kaart` is de naam van de class.

+ Maak een nieuwe class `Spel` en neem hierin een `__init__` methode op. Deze keer hebben we geen andere parameters nodig dan `self`, wat verplicht is.

```python
class Spel:

    def __init__(self):
```

+ Het `Spel` moet een lijst met kaarten opslaan, die elk een `Kaart` object zullen zijn. Voeg een attribuut met de naam `_kaarten` aan de methode `__init__` en definieer het voorlopig als een lege lijst.

```python
class Spel:

    def __init__(self):
        self._kaarten = []
```

+ Laten we nu een methode schrijven om het spel te vullen met de 52 benodigde kaarten. Begin met het maken van een methode met de naam `bevolk`:

```Python
def bevolk(self):
```

+ Definieer binnen je methode twee lijsten. De ene moet alle mogelijke kaartenkleuren bevatten en de andere alle mogelijke kaartnummers, als tekenreeksen:

```Python
def bevolk(self):
    kleuren = ["harten", "klaveren", "ruiten", "schoppen"]
    nummers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H", "A"]
```

--- collapse ---
---
title: Is er een efficiëntere manier om de lijst met nummers te maken?
---

Ja! In plaats van ze allemaal op te schrijven, kunt je **list comprehension (lijstbegrip)** gebruiken, wat een snelle manier is om een nieuwe lijst te maken op basis van een bestaande lijst.

Om een lijst met de getallen 2 tot 10 als tekenreeksen te maken, kun je dus de code gebruiken:

```Python
nummers = [str (n) for n in range(2,11)]
```

Dit betekent:
- Geef me `str (n)` (de stringversie van n)
- Voor elke `n in range(2, 11)` (onthoud dat de functie `range() (bereik)` begint bij 2 en stopt bij (maar niet inbegrepen) 11)

Voeg vervolgens een lijst toe met de plaatjes en de aas aan het einde:

```Python
nummers = [str (n) for n in range(2,11)] + ["B", "V", "H", "A"]
```

--- /collapse ---

+ Zodat `bevolk` het kaartspel genereert, moeten we alleen items uit de twee lijsten combineren — maak voor elke kleur, voor elk nummer, een `Kaart` object. Een manier om dit te doen is met geneste lussen:

```Python
kaarten = [] # Maak een lege lijst met kaarten
for kleur in kleuren: # Voor elke kleur...
    for nummer in nummers: # Voor elk nummer...
        # Maak een nieuw kaartobject en voeg dit toe aan de lijst
        kaarten.append(Kaart(kleur, nummer))  
self._kaarten = kaarten # Laat vervolgens self._kaart naar deze lijst wijzen
```

Het gebruik van geneste lussen kan je code echter ingewikkelder maken. Om de code te vereenvoudigen, kun je gebruik maken van **list comprehension (lijstbegrip)**:

```Python
self._kaarten = [Kaart(s, n) for s in kleuren for n in nummers]
```

Deze code betekent:
- Zet `self._kaarten` op
- `[ een lijst ]`
- van `Kaart` objecten
- met elke combinatie van `s, n`, loop door `for s in kleuren` en `for n in nummers`

Als je meer wilt weten over lijstbegrippen, bekijk dan onderstaande informatie.

[[[generic-python-simple-list-comprehensions]]]

+ Laten we testen of je methode een spel correct construeert. Ga terug naar je `__init__` methode, roep de `bevolk()` methode aan en druk de lijst met kaarten af:

```Python
def __init__(self):
    self._kaarten = []
    self.bevolk()
    print(self._kaarten)
```

+ Maak een instantie van de class `Spel` om te controleren of je het spel krijgt dat je wilt.

--- hints ---


--- hint ---

Maak een instantie van een class door een variabele te declareren en deze gelijk te maken aan `Class()`.

--- /hint ---

--- hint ---

Bekijk hoe je een object van class `Kaart` hebt geïnstantieerd.

--- /hint ---

--- hint ---

Gebruik deze code:

```Python
mijn_spel = Spel()
```

--- /hint ---

--- /hints ---

Je zou de volgende uitvoer moeten zien:

```Python
[2 van harten, 3 van harten, 4 van harten, 5 van harten, 6 van harten, 7 van harten, 8 van harten, 9 van harten, 10 van harten, B van harten, V van harten, H van harten, A van harten, 2 van klaveren, 3 van klaveren, 4 van klaveren, 5 van klaveren, 6 van klaveren, 7 van klaveren, 8 van klaveren, 9 van klaveren, 10 van klaveren, B van klaveren, V van klaveren, H van klaveren, A van klaveren, 2 van ruiten, 3 van ruiten, 4 van ruiten, 5 van ruiten, 6 van ruiten, 7 van ruiten, 8 van ruiten, 9 van ruiten, 10 van ruiten, B van ruiten, V van ruiten, H van ruiten, A van ruiten, 2 van schoppen, 3 van schoppen, 5 van schoppen, 6 van schoppen, 7 van schoppen, 8 van schoppen, 9 van schoppen, 10 van schoppen, B van schoppen, V van schoppen, H van schoppen, A van schoppen]
```
