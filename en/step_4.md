## Instantiate an object

<video width="560" height="315" controls>
<source src="resources/clip2.mp4" type="video/mp4">
Your browser does not support the video tag, try FireFox or Chrome
</video>

Let's test out the `Card` class by creating a card object. This object is an **instance** of the `Card` class, so creating the object is also called **instantiating** the object.

+ Underneath your class definition, create a `Card` object called `my_card` which will be the 6 of hearts:

```python
my_card = Card("hearts", "6")
```

+ Add a print statement to display the card object

```python
print(my_card)
```

+ Run the program. You will see the text representation of your object - it is a `Card` and you are shown the address of the object in memory.

You can **override** the `__repr__` method to change how your object is represented as text.

+ Go back to your class definition and add in some code to override the `__repr__` method so that it describes the card:

```python
def __repr__(self):
    return self.number + " of " + self.suit
```

For example, this will print "5 of spades" if `self.number` is `"5"` and `self.suit` is `"spades"`.

+ Run the program again and check that your new way of representing the object as text works.
