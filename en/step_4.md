## Instantiate an object

<video width="560" height="315" controls>
<source src="resources/clip2.mp4" type="video/mp4">
Your browser does not support the video tag, so try FireFox or Chrome.
</video>

Let's test out our `Card` class by creating a card object. The object is an **instance** of the `Card` class, and creating it is also called **instantiating**.

+ Below your class definition, instantiate a card object called `my_card` for the 6 of Hearts:

```python
my_card = Card("hearts", "6")
```

You may be wondering why the card number is `"6"` (a string) and not `6` (an integer). This is because some of the card "numbers" will be `"J"`, `"Q"`, `"K"` and `"A"`!

+ Add a print statement to display the card object.

```python
print(my_card)
```

+ Run the program. You will see the text representation of your object — it is a `Card`, and you are shown the address of the object in memory.

You can **override** the `__repr__` method to change how your object is represented as text.

+ Go back to your class definition and add in some code to override the `__repr__` method so that it describes the card:

```python
def __repr__(self):
    return self.number + " of " + self.suit
```

For example, if `self.number` is `"5"` and `self.suit` is `"spades"`, this will print "5 of spades".

+ Run the program again and check that your new way of representing the object as text works. You can also customise this representation to your own liking.
