## Attributen en eigenschappen

Dus je kunt de attributen binnen een object veranderen, je klasse heeft wat **eigenschappen** nodig.

Eigenschappen zijn de speciale methoden die de waarde van een attribuut ofwel **get (krijgen)** of **set (instellen)**, en worden daarom de **getter** en de **setter** genoemd.

### Getters en setters

Voor dit gedeelte kun je de onderstaande video (in het Engels) bekijken of de schriftelijke instructies volgen.

<video width="768" height="576" controls>
<source src="resources/clip3.mp4" type="video/mp4">
Je browser ondersteunt de video-tag niet, probeer Firefox of Chrome
</video>

Het is mogelijk om rechtstreeks toegang te krijgen tot de attributen van een object. Bijvoorbeeld, kun je de volgende code aan de onderkant van je programma toevoegen om het `kleur` attribuut van `mijn_kaart` te veranderen en vervolgens het object weer te geven:

```python
mijn_kaart.kleur = "klaveren"
print(mijn_kaart)
```

Rechtstreeks toegang krijgen tot attributen is echter geen goed idee, omdat mensen dit soort dingen zouden kunnen doen:

```python
mijn_kaart.kleur = "dinosaurussen"
print(mijn_kaart)
```

Laten we in plaats daarvan eigenschappen voor je klasse maken: een **getter** en een **setter** voor toegang tot het attribuut `kleur`.

+ Voordat we hiermee beginnen, ga je terug naar je `__init__` methode en zoek je `self.kleur`. Voeg een onderstrepingsteken `_` toe voor `kleur` om aan te geven dat je niet wilt dat mensen rechtstreeks toegang hebben tot dit kenmerk.

```python
def __init__(self, kleur, nummer):
    self._kleur = kleur
```

--- collapse ---
---
title: Betekent het onderstrepingsteken dat het attribuut niet rechtstreeks kan worden gewijzigd?
---

Een onderstrepingsteken toevoegen is een goed gebruik en een goede programmeerstijl.

Het onderstrepingsteken **verhindert echter niet dat** mensen het attribuut rechtstreeks wijzigen — het is een conventie die aangeeft dat zij dat **niet moeten** doen. Als je dit wilt testen, voeg je een onderstrepingsteken toe aan je code om het attribuut te wijzigen in `"dinosaurussen"`:

```python
mijn_kaart._kleur = "dinosaurussen"
```

Je zult zien dat je het attribuut nog steeds kunt wijzigen, net als voorheen.

--- /collapse ---

#### Een getter maken

+ Ga terug naar je `Kaart` classdefinitie, voeg een nieuwe methode toe met de naam `kleur`en laat deze de waarde van het kenmerk `_kleur` retourneren.

```python
def kleur(self):
    return self._kleur
```

+ Voeg een **decorator** aan deze methode om te zeggen dat het een eigenschap is.

```python
@property
def kleur(self):
    return self._kleur
```

Wanneer iemand nu de waarde `mijn_kaart.kleur` in zijn programma gebruikt, wordt deze getter aangeroepen en ontvangt de gebruiker de waarde `self._kleur` opgeslagen in het `mijn_kaart` object.

--- collapse ---
---
title: Wat is een decorator?
---

In objectgeoriënteerd programmeren kun je met decorators extra gedrag (of functionaliteit) aan een class toevoegen.

Een decorator kan worden gezien als een wikkel voor een methode: het bevat de methode, maar het breidt ook de functionaliteit uit.

De decorator `@property` in Python moet worden toegevoegd aan de getter-methode om de methode als een eigenschap te definiëren.

--- /collapse ---

#### Een setter maken

+ Voeg nog een methode toe. Het is belangrijk dat deze methode **ook `kleur`** heet. Er moeten gegevens worden gebruikt die de nieuwe kleur vertegenwoordigen die de gebruiker wil instellen en een basiscontrole uitvoeren om te controleren of de gegevens een van de gebruikelijke kleuren zijn die beschikbaar zijn in een stapel kaarten.

```python
def kleur(self, kleur):
    if kleur in ["harten", "klaveren", "ruiten", "schoppen"]:
        self._kleur = kleur
    else:
        print("Dat is geen kleur!")
```
+ Voeg nu een decorator toe aan deze methode om te zeggen dat dit de setter is voor `kleur`.

```Python
@kleur.setter
def kleur(self, kleur):
```

Net als bij de getter-methode definieert deze decorator de methode als een eigenschap. Wanneer iemand nu het kenmerk `kleur` probeert in te stellen (bijvoorbeeld door `mijn_kaart.kleur = "schoppen"` te typen), wordt de eigenschap `@kleur.setter` aangeroepen. In dit voorbeeld wordt de waarde `"schoppen"` doorgegeven als de parameter `kleur`.

Merk op dat door het gebruik van getter- en setter-eigenschappen en decorators, je twee functies kunt hebben met dezelfde naam, een die wordt aangeroepen wanneer je de waarde krijgt en een die wordt aangeroepen wanneer je de waarde instelt.

--- collapse ---
---
title: Waarom gebruiken we eigenschappen?
---

Waarom zouden we de decorators `@property` en `.setter` willen gebruiken om eigenschappen te maken in plaats van alleen een methode `get_kleur()` en een methode `set_kleur()` te maken?

Er zijn verschillende redenen:

- Het is korter en mooier om te kunnen verwijzen naar `kaart.kleur` plaats van `kaart.get_kleur()` en `kaart.set_kleur()`. Bijvoorbeeld:

```python
mijn_kleur = kaart.kleur
kaart.kleur = "schoppen"
```

is veel netter dan:

```python
mijn_kleur = kaart_get_kleur()
kaart.set_kleur("schoppen")
```

- Je kunt complexe functies eruit laten zien als eenvoudige bewerkingen. Denk terug aan het LED-voorbeeld in stap 1: je hoeft niet te weten hoe je een LED kunt inschakelen met je computer – `on()` doet het allemaal voor je.

- Als je eigenschappen gebruikt in plaats van directe toegang tot attributen toe te staan en je moet de werking van de class wijzigen, kun je dit doen zonder de code te breken die de class gebruikt. De oorspronkelijke `kleur` setter die je hebt geschreven, heeft de kleur bijvoorbeeld eenvoudig opgeslagen, maar laten we zeggen dat je deze in hoofdletters wilt opslaan. Om dit te doen, kun je gewoon de code binnen de eigenschap wijzigen:

```python
@kleur.setter
def kleur(self, kleur):
        if kleur in ["harten", "klaveren", "ruiten", "schoppen"]:
            self._kleur = kleur.upper()
        else:
            print("Dat is geen kleur!")
```

Nu worden alle kleuren opgeslagen als hoofdletters, terwijl elke code die de eigenschap `kleur` gebruikt, nog steeds werkt.

Als je mensen rechtstreeks toegang geeft tot het attribuut `kleur`, kun je later geen enkel aspect van de code wijzigen.

--- / collapse ---

+ Voer het programma uit. Als je nu probeert de kaartkleur te veranderen in iets anders dan een van de kleuren in de lijst, zou je `"Dat is geen kleur!"` moeten zien verschijnen en de kleur mag niet veranderen.

Merk op dat je momenteel geen validatie hebt in de `__init__` methode, dus je kunt nog steeds de 2 van Dinosaurussen als volgt maken:

```Python
andere = Kaart("Dinosaurussen", "2")
```
