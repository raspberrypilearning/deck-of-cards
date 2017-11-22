## Create a class

A **class** is like a blueprint for creating **objects**. I like to think of a class as being similar to a cookie cutter – it is a template for all the cookie objects you make.

<video width="560" height="315" controls>
<source src="resources/clip1.mp4" type="video/mp4">
Your browser does not support the video tag, try FireFox or Chrome
</video>

We are going to begin by making a `Card` class which will act as a template for all playing card objects.

![Five of spades](images/five-of-spades.png)

+ Open a new Python file and save it as `card.py`

+ Begin by creating a `Card` class

```python
class Card:
```

Class names are usually written with a capital letter so that they are easily distinguishable from variable names.

In Python, every object has a special method called `__init__` which tells it how to create (or **initialise**) itself. The method name has a double underscore either side of the word `init`.

+ Create an `__init__` method for your object




You can make as many instances of cookie objects as you want, and they will all start off from the same template. If you like, you can customise each instance of a cookie object, perhaps by adding some icing or some sprinkles. But whenever you make cookies, you use the same cookie-cutter template.
