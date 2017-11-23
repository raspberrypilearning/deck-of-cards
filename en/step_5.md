## Setters and getters

<video width="560" height="315" controls>
<source src="resources/clip2.mp4" type="video/mp4">
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

Note that this **will not prevent** people from accessing the attribute - try typing `my_card._suit = "crocodiles"` to change the attribute - but it is a convention which indicates that they should not.

+ Add a new method
