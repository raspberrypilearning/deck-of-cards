## Create a class

A **class** is like a template for creating **objects**. You are going to begin by making a `Card` class which will act as a template for creating playing card objects.

Each card object is a separate **instance** of the `Card` class. You might have a card object representing the 5 of Spades and a card object representing the 2 of Hearts.

Our playing cards will be represented as text rather than a picture like the card below.

![Five of spades](images/five-of-spades.png)

### Create a class

You can choose whether to watch the video or use the written instructions.

<video width="560" height="315" controls>
<source src="resources/clip1.mp4" type="video/mp4">
Your browser does not support the video tag, try FireFox or Chrome
</video>

+ Open a new Python file and save it as `card.py`

+ Begin by creating a `Card` class

```python
class Card:
```

Class names are usually written with a capital letter so that they are easily distinguishable from variable names.

### Create an `__init__` method

In Python, every object has a special **method** called `__init__` which tells it how to create (or **initialise**) itself. Methods are very similar to functions, and we use them to interact with the object. This method name has a double underscore either side of the word `init`.

+ Create an `__init__` method for your object

```python
class Card:
    def __init__(self):
```

--- collapse ---
---
title: Why do I need the self parameter?
---
You might be wondering why you need to put `self` as the first parameter. A method is just a function, but it needs context in order to work.

The first argument in a method must always be `self` because the object itself is always automatically passed in as the first argument, followed by any other arguments.

--- /collapse ---

### Attributes

Attributes are pieces of information stored within an object, rather like a collection of variables associated with that object. The card object will begin with two attributes - `suit` and `number`, and we will prefix them with `self.` to show that they belong to the object instance.

+ Add two attributes to your `__init__` method, and two parameters so that you can pass in their values as arguments when you create the object:

```python
def __init__(self, suit, number):
    self.suit = suit
    self.number = number
```
