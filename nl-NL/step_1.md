## Inleiding

Maak een model van een kaartspel dat de basis kan vormen voor het bouwen van programma's voor digitale kaartspellen zoals Poker of Gin Rummy.

### Wat ga je maken

Je leert hoe je het objectgeoriënteerde programmeerparadigma in Python kunt gebruiken om een herbruikbaar model van een kaartspel te maken.

Object-georiënteerd programmeren (OOP) is een manier om je code te organiseren, zodat deze gemakkelijker te begrijpen, opnieuw te gebruiken en te wijzigen is. Met OOP kun je gegevens (variabelen) en functionaliteit combineren en ze samenbrengen in **objecten**.

![Kaarten](images/cards.jpg)

_Afbeelding door Rosapicci (eigen werk) [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons_

--- collapse ---
---
title: Wat is objectgeoriënteerd programmeren?
---

Je hebt waarschijnlijk gehoord van objectgeoriënteerd programmeren, maar misschien weet je niet zeker wat het is. Misschien heb je zelfs geprobeerd om gidsen of boeken te lezen, maar verdwaalde je in het jargon.

Objectgeoriënteerd programmeren is een integraal onderdeel van veel programmeertalen en het is gewoon een andere stijl van programmeren.

#### Wat is een object?

Objecten worden gebruikt om dingen in code te modelleren. Een object kan een fysiek item vertegenwoordigen, zoals een LED, of het kan een digitale eenheid vertegenwoordigen, zoals een bankrekening of een personage in een computerspel. Een object is in feite een groep gegevens en functies. Omdat je jouw eigen objecten kunt definiëren, kun je alles wat je maar wilt met een object weergeven!

#### Waar zou ik eerder objecten hebben gezien?

Laten we eens kijken naar een voorbeeld van een LED die is aangesloten op een Raspberry Pi-computer. Maak je geen zorgen als je nog nooit een LED hebt aangesloten of andere physical computing hebt gedaan — het belangrijkste is hier de code!

![led verbonden met pin 17](images/LED-GP17.gif)

Links in het diagram bevinden zich de GPIO-pinnen van de Raspberry Pi, waarmee we componenten kunnen bedienen die erop zijn aangesloten. De LED is verbonden met pin 17. Om de LED in te schakelen, zou je de volgende Python-code gebruiken:

```python
from gpiozero import LED
rood = LED(17)           
rood.on()
```

Voor interactie met de LED hebben we een `LED` object gemaakt dat de fysieke LED in code vertegenwoordigt. Het heeft de naam `rood` zodat we naar dat specifieke LED-object kunnen verwijzen.

```python
rood = LED(17)
```

We kunnen een andere LED aansluiten op pin 21 en vervolgens een ander object maken met een andere naam om het te vertegenwoordigen:

```python
groen = LED(21)
```

#### Waarom zou ik objecten willen gebruiken?

In ons voorbeeld hebben we een `LED` object gemaakt om een fysieke LED in code te modelleren. We hebben ook een commando opgenomen om de LED te besturen, in dit geval om deze `on (aan)` te zetten. Dergelijke opdrachten worden methoden genoemd — aangepaste functies die specifiek zijn ontworpen om te communiceren met een object.

Een van de voordelen van het gebruik van objectgeoriënteerd programmeren is dat onnodige details kunnen worden weggelaten als we een methode gebruiken. We hoeven niet precies te weten hoe een methode precies werkt om deze te kunnen gebruiken, we kunnen het gewoon aanroepen om een gewenst resultaat te bereiken. In ons voorbeeld hoeven we niets te weten over de `on()` methode, afgezien van het feit dat het gebruiken op ons `LED` object de fysieke LED zal doen oplichten.

--- /collapse ---

### Wat ga je leren

Dit project behandelt elementen uit de volgende onderdelen van de [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum){:target="_blank"}:

+ [Pas hogere programmeertechnieken toe om problemen in de echte wereld op te lossen](https://curriculum.raspberrypi.org/programming/maker/){:target="_blank"}

### Aanvullende informatie voor docenten

Als je dit project wilt afdrukken, gebruik dan de [printervriendelijke versie](https://projects.raspberrypi.org/nl-NL/projects/deck-of-cards/print){:target="_blank"}.

Gebruik de link in de voettekst voor toegang tot de GitHub opslagplaats voor dit project, met daarin alle bronnen (inclusief een voorbeeld van een voltooid project) in de map 'nl-NL/resources'.
