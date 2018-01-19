## Create a class

A **class** is like a template for creating **objects**.  

Think of a class as being similar to a cookie cutter – it is a template for all the cookie objects you make. 

<video width="768" height="576" controls>
<source src="resources/Cementyourknowledgeofobjects_sd.mp4" type="video/mp4">
Your browser does not support the video tag, so try FireFox or Chrome.
</video>

You can make as many instances of cookie objects as you want, and they will all start off from the same template. 

If you like, you can customise each instance of a cookie object, perhaps by adding some icing or some sprinkles. But whenever you make cookies, you use the same cookie-cutter template.

### Create a class

You are going to begin by making a `Card` class that will act as a template for creating playing card objects.

Each card object is a separate **instance** of the `Card` class. For example, you might have a card object representing the 5 of Spades and another card object representing the 2 of Hearts.

Our playing cards will be represented as text rather than pictures like the one below.

![Five of spades](images/five-of-spades.png)

You can choose whether to watch the video or to use the written instructions.

<video width="560" height="315" controls>
<source src="resources/clip1.mp4" type="video/mp4">
Your browser does not support the video tag, so try FireFox or Chrome.
</video>

+ Open a new Python file and save it as `card.py`.

+ Begin by creating a `Card` class:

```python
class Card:
```

Class names are usually written with a capital letter so that they are easily distinguishable from variable names.

### Methods

You may have already encountered functions when writing Python code. Functions allow us to give a name to a set of instructions. You can pass data to a function as parameters, and optionally you can have it return some data as a result.

The difference is that a method is called on an object, which means that as well as being able to receive data from outside the object as paramters, a method can use all of the data stored inside the object as well.

### Create an `__init__` method

In Python, every class has a special **method** called `__init__` that tells it how to create (or **initialise**) itself. Methods are very similar to functions, and we use them to interact with objects. This particular method name always has a double underscore on either side of `init`.

+ Create an `__init__` method for your object:

```python
class Card:
    def __init__(self):
```

--- collapse ---
---
title: Why do I need the `self` parameter?
---
A method is just a function, but it needs context in order to work. The first argument in any `Class` method must always be `self`, because the object itself is always automatically passed in as the first argument, followed by any other arguments.

`self` is the reference to the **object** which is initialised from the **class**, and this is how data and functions are shared across the **object**.

Let's look at an example:

Outside of OOP, for two functions to share the same variable, it must be global:

```python
name = "Laura"

def hi():
    print("Hi " + name)

def bye():
    print("Bye " + name)
```

Within a **class**, `self` can be used to share variables:

```python
class Welcome():
    def __init__(self):
        self.name = "Laura"

    def hi(self):
        print("Hi " + self.name)

    def bye(self):
        print("Bye " + self.name)
```

--- /collapse ---

### Attributes

Attributes are pieces of information stored within an object, rather like a collection of variables associated with that object. The card object will begin with two attributes, `suit` and `number`, and we will prefix them with `self.` to show that they belong to the object instance.

+ Add two attributes to your `__init__` method, and two parameters so that you can pass in their values as arguments when you create the object:

```python
def __init__(self, suit, number):
    self.suit = suit
    self.number = number
```
