## Attributes and properties

So you can change the attributes within an object, your class will need some **properties**. These are the special methods that either **get** or **set** the value of an attribute, and are therefore referred to as the **getter** and the **setter**.

### Getters and setters

For this section, you can either watch the video below, or read the instructions.

<video width="768" height="576" controls>
<source src="resources/clip3.mp4" type="video/mp4">
Your browser does not support the video tag, try FireFox or Chrome
</video>

It is possible to access the attributes of an object directly. For example, you could add the following code at the bottom of your program to change the `suit` attribute of `my_card` and then display the object:

```python
my_card.suit = "clubs"
print(my_card)
```

However, accessing the attributes directly is not a good idea, because it allows people to do things like this:

```python
my_card.suit = "dinosaurs"
print(my_card)
```

Instead, let's create properties for your class: a **getter** method and a **setter** method for accessing the `suit` attribute.

+ First, go back to your `__init__` method and locate `self.suit`. Add an underscore before `suit` to indicate that you do not want people to access this attribute directly.

```python
def __init__(self, suit, number):
    self._suit = suit
```

--- collapse ---
---
title: Does the underscore mean the attribute cannot be changed directly?
---
No. This **will not prevent** people from changing the attribute directly, but it is a convention which indicates that they **should not**. If you want to test this, add an underscore to your code for changing the attribute to `"dinosaurs"`:

```python
my_card._suit = "dinosaurs"
```

You will see that you can still change the attribute just as before.

--- /collapse ---

### Getter

+ Go back to your `Card` class definition, add a new method called `suit`, and have it return the value of the `_suit` attribute.

```python
def suit(self):
    return self._suit
```

+ Add a **decorator** to this method to say that it is a property.

```python
@property
def suit(self):
    return self._suit
```

Now, wherever someone uses the value `my_card.suit` in their program, this getter method will be called, and the user will receive the value of `self._suit` stored within the `my_card` object. 

--- collapse ---

---
title: What's a decorator, and what does the `@property` decorator do?
---

In object-oriented programming, decorators allow you to add additional behaviour (or functionality) to a class.

A decorator can be thought of as a wrapper to a method: it contains the method but it also extends its functionality.

The `@property` decorator in Python needs to be added to the getter method so that the method 'becomes' a property.

--- /collapse ---

### Setter

+ Add another method. It is important that this method **is also called `suit`**. It should take a piece of data representing the new suit the user would like to set, and do a basic check to make sure that the piece of data is one of the usual suits available in a deck of cards.

```python
def suit(self, suit):
    if suit in ["hearts", "clubs", "diamonds", "spades"]:
        self._suit = suit
    else:
        print("That's not a suit!")
```
+ Now add a decorator to this method to say that it is the setter for the attribute `suit`.

```Python
@suit.setter
def suit(self, suit):
```

As with the getter method, this decorator defines the method as a property. Now whenever someone tries to set the `suit` attribute, e.g. by typing `my_card.suit = "spades"`, the `@suit.setter` property will be called, and in this example, the value of `"spades"` will be passed to it as the `suit` parameter.

+ Run the program. If you now try to change the card's suit to anything other than one of the suits in the list, you should see `"That's not a suit!"` appear, and the suit should not change.

Note that we don't currently have any validation in the `__init__` method, so if you can still create the 2 of Dinosaurs like this:

```Python
another_card = Card("Dinosaurs", "2")
```

--- collapse ---
---
title: What is the point of properties?
---
Why would we want to use the `@property` and `@suit.setter` decorators to create properties instead of just writing `get_suit()` and `set_suit()` methods?

There are several reasons why:

- It's shorter and nicer to be able to refer to `card.suit` rather than `card.get_suit()`.

- You can use `card.suit` in two different contexts, but with identical syntax:

```Python
# Set the suit of this card
card.suit = "clubs"

# Get the suit of this card
print(card.suit)
```

- Most importantly, if you have used properties and you need to change how the properties work, you can do so without breaking any code that uses the class. For example, the original `suit` property you wrote simply returned the suit, but let's say you want to return it in capitals. To do so, you can just change the code within the property:

```python
@property
def suit(self):
    return self._suit.upper()
```

Any code which uses the `suit` property will still work. However, if you had just let people access the `suit` attribute directly, you would not be able to change its implementation later.

--- /collapse ---
