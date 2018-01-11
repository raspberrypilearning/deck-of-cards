## Setters and getters

<video width="560" height="315" controls>
<source src="resources/clip3.mp4" type="video/mp4">
Your browser does not support the video tag, try FireFox or Chrome
</video>

It is possible to access the attributes of an object directly. For example you could add this code at the end of your program to change the suit of the card and then display it:

```python
my_card.suit = "clubs"
print(my_card)
```

However, accessing the attributes directly is not a good idea because it allows people to do things like this:

```python
my_card.suit = "dinosaurs"
print(my_card)
```

Instead, let's create a **setter** and a **getter** for the suit.

+ Go back to your `__init__` method and locate `self.suit`. Add an underscore before `suit` to indicate that you do not want people to access this attribute directly.

```python
def __init__(self, suit, number):
    self._suit = suit
```
--- collapse ---
---
title: Does the underscore mean the attribute cannot be changed directly?
---
No. This **will not prevent** people from accessing the attribute, but it is a convention which indicates that they _should not_. If you want to test this, try adding an underscore to your code which changes the attribute:

```python
my_card._suit = "dinosaurs"
```

...and you will see that you can still change the attribute just as before.

--- /collapse ---

### Getter

+ Go back to your `Card` class definition and add a new method called `suit` which returns the value of the `_suit` attribute.

```python
def suit(self):
    return self._suit
```

+ Add a **decorator** to this method to say that it is a **property**.

```python
@property
def suit(self):
    return self._suit
```

This means that wherever someone uses the value `my_card.suit` in their program, this function will be called, in this case they will receive the value of `self._suit`. Decorators are language-specific to Python.

### Setter

+ Add another new method, and it is important that this method **is also called `suit`**. This method should take a piece of data passed in to represent the new suit they would like to set, and I am going to do a basic check to make sure that this data is one of the usual suits available in a deck of cards.

```python
def suit(self, suit):
    if suit in ["hearts", "clubs", "diamonds", "spades"]:
        self._suit = suit
    else:
        print("That's not a suit!")
```
+ Now add a decorator to this method to say that it is the **setter** for the property **suit**.

```Python
@suit.setter
def suit(self, suit):
```

This means that when someone types `my_card.suit = "spades"` (i.e. tries to **set** the `suit` property) then this function will be called, with the value of "spades" sent in to the function as the `suit` parameter.

+ Run the program - you should see `"That's not a suit!"` appear if you try to change the card's suit to anything other than one of the suits in the list, and the suit will not change.

Note that we don't currently have any validation in the `__init__` method, so if you create the 2 of Dinosaurs like this, it will still work!

```Python
another_card = Card("Dinosaurs", "2")
```

--- collapse ---
---
title: What is the point of the @property decorator?
---
You might ask what is the point of using the `@property` and `@suit.setter` decorators - why don't we just write `get_suit()` and `set_suit()` methods?

There are several reasons why:

- It's shorter and nicer to be able to refer to `card.suit` rather than `card.get_suit()`

- You can use `card.suit` in two different contexts, but the syntax is identical:

```Python
# Set the suit of this card
card.suit = "clubs"

# Get the suit of this card
print(card.suit)
```

- If you need to change the implementation of your class, if you have used properties you can do that without breaking any code which uses the class.

The original `suit` property we wrote simply returned the suit, but let's say you wanted to return it in capitals, you could just change the code inside the property:

```python
@property
def suit(self):
    return self._suit.upper()
```

Any code which uses the `suit` property would still work and this change would be applied everywhere. However, if you had just let people access the `suit` property directly, you would not be able to later change its implementation.

--- /collapse ---
