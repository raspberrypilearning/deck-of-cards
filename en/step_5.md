## Attributes and properties

So you can change the attributes within an object, your class will need some **properties**. 

Properties are the special methods that either **get** or **set** the value of an attribute, and are therefore referred to as the **getter** and the **setter**.

### Getters and setters

For this section, you can either watch the video below, or follow the written instructions.

<video width="768" height="576" controls>
<source src="resources/clip3.mp4" type="video/mp4">
Your browser does not support the video tag, try FireFox or Chrome
</video>

It is possible to access the attributes of an object directly. For example, you could add the following code at the bottom of your program to change the `suit` attribute of `my_card` and then display the object:

```python
my_card.suit = "clubs"
print(my_card)
```

However, accessing attributes directly is not a good idea, because people could do things like this:

```python
my_card.suit = "dinosaurs"
print(my_card)
```

Instead, let's create properties for your class: a **getter** and a **setter** for accessing the `suit` attribute.

--- task ---

Before we start on this, go back to your `__init__` method and locate `self.suit`. Add an underscore `_` before `suit` to indicate that you do not want people to access this attribute directly.

```python
def __init__(self, suit, number):
 self._suit = suit
```

--- collapse ---
---
title: Does the underscore mean the attribute cannot be changed directly?
---
Adding an underscore is good practice and good programming style.

However, the underscore **will not prevent** people from changing the attribute directly — it is a convention which indicates that they **should not** . If you want to test this, add an underscore to your code for changing the attribute to `"dinosaurs"`:

```python
my_card._suit = "dinosaurs"
```

You will see that you can still change the attribute just as before.

--- /collapse ---

#### Creating a getter

--- /task ---

--- task ---

Go back to your `Card` class definition, add a new method called `suit`, and have it return the value of the `_suit` attribute.

```python
def suit(self):
 return self._suit
```

--- /task ---

--- task ---

Add a **decorator** to this method to say that it is a property.

```python
@property
def suit(self):
 return self._suit
```

Now, whenever someone uses the value `my_card.suit` in their program, this getter will be called, and the user will receive the value of `self._suit` stored within the `my_card` object. 

--- collapse ---

---
title: What's a decorator?
---

In object-oriented programming, decorators allow you to add additional behaviour (or functionality) to a class.

A decorator can be thought of as a wrapper to a method: it contains the method but it also extends its functionality.

The `@property` decorator in Python needs to be added to the getter method to define the method as a property.

--- /collapse ---

#### Creating a setter

--- /task ---

--- task ---

Add another method. It is important that this method **is also called `suit`**. It should take a piece of data representing the new suit the user would like to set, and do a basic check to make sure that the piece of data is one of the usual suits available in a deck of cards.

```python
def suit(self, suit):
 if suit in ["hearts", "clubs", "diamonds", "spades"]:
 self._suit = suit
 else:
 print("That's not a suit!")
```

--- /task ---

--- task ---

Now add a decorator to this method to say that it is the setter for `suit`.

```Python
@suit.setter
def suit(self, suit):
```

As with the getter method, this decorator defines the method as a property. Now, whenever someone tries to set the `suit` attribute (e.g. by typing `my_card.suit = "spades"`), the `@suit.setter` property will be called. In this example, the value `"spades"` will be passed to it as the `suit` parameter.

Notice that by using getter and setter properties and decorators, you can have two functions with the same name, one which is called when you get the value, and one which is called when you set the value.

--- collapse ---

---
title: Why do we use properties?
---

Why would we want to use the `@property` and `.setter` decorators to create properties instead of just creating a `get_suit()` method and a `set_suit()` method?

There are several reasons:

- It's shorter and nicer to be able to refer to `card.suit` rather than `card.get_suit()` and `card.set_suit()`. For example:

```python
my_suit = card.suit
card.suit = "spades"
```

is much neater than:

```python
my_suit = card.get_suit()
card.set_suit("spades")
```

- You can make complex functions look like simple operations. Think back to the LED example on step 1: you don't need to know the details of how to turn on an LED with your computer – `on()` does it all for you. 

- If you use properties rather than allowing direct access to attributes and you need to change how the class works, you can do so without breaking any code that uses the class. For example, the original `suit` setter you wrote simply stored the suit, but let's say you want to store it in capital letters. To do so, you can just change the code within the property:

```python
@suit.setter
def suit(self, suit):
 if suit in ["hearts", "clubs", "diamonds", "spades"]:
 self._suit = suit.upper()
 else:
 print("That's not a suit!")
```

Now all suits will be stored as capitals, while any code that uses the `suit` property will still work.

If you let people access the `suit` attribute directly, you will not be able to change any aspects of its code later.

--- /collapse ---

--- /task ---

--- task ---

Run the program. If you now try to change the card's suit to anything other than one of the suits in the list, you should see `"That's not a suit!"` appear, and the suit should not change.

Note that you currently don't have any validation in the `__init__` method, so you could still create the 2 of Dinosaurs like this:

```Python
another_card = Card("Dinosaurs", "2")
```

--- /task ---

