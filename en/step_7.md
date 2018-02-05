## A deck of cards

Now that you have a basic model of a card, it's time to create a deck.

+ Create a `Deck` class. You can either do this in the same file where you wrote your `Card` class, or in a separate one. If you do it in a different file (e.g. `deck.py`), you will need to import the class at the top of your `card.py` file with this code:

```python
from deck import Deck
```

In this line of code, `deck` is the name of the Python file containing the class, minus the `.py` extension, and `Deck` is the name of the class.

+ Create an `__init__` method for your `Deck`. This time we won't need any parameters other than `self`, which is compulsory.

```python
class Deck:

    def __init__(self):
```

+ The `Deck` will need to store a list of cards, each of which will be a `Card` object. Add an attribute called `_cards` to the `__init__` method, and define it as an empty list for now.

```python
class Deck:

    def __init__(self):
        self._cards = []
```

+ Now let's write a method to populate the deck with the 52 necessary cards. Begin by creating a method called `populate`:

```Python
def populate(self):
```

+ Inside your method, define two lists. One should contain all the possible card suits, and the other all the possible card numbers, as strings:

```Python
def populate(self):
    suits = ["hearts", "clubs", "diamonds", "spades"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
```

--- collapse ---
---
title: Is there a more efficient way to make the list of numbers?
---
Yes! Instead of writing them all out, you could use a **list comprehension**, which is a quick way of creating a new list based on an existing list.

So, to create a list containing the numbers 2 to 10 as strings, you could use the code:

```Python
numbers = [str(n) for n in range(2,11)]
```

This means:
- Give me `str(n)` (the string version of n)
- For every `n in range(2, 11)` (remember that the `range()` function will start at 2 and stop at (but not include) 11)

Then add a list containing the picture cards and the ace at the end:

```Python
numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
```

--- /collapse ---

+ So that `populate` generates the deck of cards, we just have to combine items from the two lists — for each suit, for each number, create a `Card` object. One way of doing this is with nested loops:

```Python
cards = []                          # Create an empty list of cards
for suit in suits:                  # For each suit...
    for number in numbers:          # For each number...
        # Create a new Card object and add it to the list
        cards.append( Card(suit, number) )  
self._cards = cards                 # Then point self._cards at this list
```

However, using nested loops can make your code more complicated and it is possible to use *list comprehension* to simplify the code:

```Python
self._cards = [ Card(s, n) for s in suits for n in numbers ]
```

This code means:
- Set `self._cards` to
- `[ a list ]`
- of `Card` objects
- containing every combination of `s, n`, looping through `for s in suits` and `for n in numbers`

If you would like to know more about list comprehensions, have a look at the information below.

[[[generic-python-simple-list-comprehensions]]]

+ Let's test whether your method properly constructs a deck. Go back to your `__init__` method, call the `populate()` method, then print out the list of cards:

```Python
def __init__(self):
    self._cards = []
    self.populate()
    print(self._cards)
```

+ Create an instance of the `Deck` class to check whether you are getting the deck you want.

--- hints ---

--- hint ---

You create an instance of a class by declaring a variable and making it equal to `Class()`.

--- /hint ---

--- hint ---

Review how you instantiated an object of the `Card` class.

--- /hint ---

--- hint ---

Use this code:

```Python
my_deck = Deck()
```

--- /hint ---

--- /hints ---

You should see the following output:

```Python
[2 of hearts, 3 of hearts, 4 of hearts, 5 of hearts, 6 of hearts, 7 of hearts, 8 of hearts, 9 of hearts, 10 of hearts, J of hearts, Q of hearts, K of hearts, A of hearts, 2 of clubs, 3 of clubs, 4 of clubs, 5 of clubs, 6 of clubs, 7 of clubs, 8 of clubs, 9 of clubs, 10 of clubs, J of clubs, Q of clubs, K of clubs, A of clubs, 2 of diamonds, 3 of diamonds, 4 of diamonds, 5 of diamonds, 6 of diamonds, 7 of diamonds, 8 of diamonds, 9 of diamonds, 10 of diamonds, J of diamonds, Q of diamonds, K of diamonds, A of diamonds, 2 of spades, 3 of spades, 4 of spades, 5 of spades, 6 of spades, 7 of spades, 8 of spades, 9 of spades, 10 of spades, J of spades, Q of spades, K of spades, A of spades]
```
