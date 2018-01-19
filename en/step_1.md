## Introduction

Create a reusable object-oriented model of a deck of cards.

### What you will make

You will learn how to use the object-oriented programming paradigm in Python to create a model of a deck of cards.

![Cards](images/cards.jpg)

Object-oriented programming (OOP) is a way of organising your code so it is easier to understand, reuse, and change.

OOP allows you to combine data (variables) and functionality and wrap them together inside **objects**.

--- collapse ---

---
title: What is object-oriented programming
---

You have probably heard of object-oriented programming, but perhaps you are unsure about what it is. Maybe you have attempted to read guides or books but got lost in the jargon. 

Object-oriented programming is integral to many programming languages and it is simply a different style of programming. 

#### What is an object?

Objects are used to model things in code. An object can represent a physical item, e.g. an LED; or a digital unit, e.g. a bank account or an enemy in a computer game. As such, an object is basically a group of data and functions. Because you can define your own objects, you can represent anything you like using an object!

#### Where would I have seen objects before?

Let’s look at an example of an LED wired up to a Raspberry Pi computer. Don’t worry if you have never wired up an LED or done any other physical computing before – the most important thing here is the code!

![led connected to pin 17](images/LED-GP17.gif)

On the left of the diagram are the Raspberry Pi’s GPIO pins, which allow us to control components that are connected to them. The LED is connected to pin 17. To make the LED switch on, you would use the following Python code:

```python
from gpiozero import LED
red = LED(17)			
red.on()
```

To interact with the LED, we have created an LED object which represents the physical LED in code. It has the name ‘red’ so that we can refer to that specific LED object.

```python
red = LED(17)
```

If we wired up another LED to pin 21, we could create another object with a different name to represent it:

green = LED(21)

#### Why would I want to use objects?

In our example, we created an LED object to model a physical LED in code. We also included a command to control the LED, in this case to turn it on. Such commands are called methods, i.e. custom functions specifically designed to interact with an object.

One of the benefits of using object-oriented programming is that unnecessary details can be abstracted away in the implementation of the methods. We do not need to know the specifics of exactly how a method works to be able to use it, we simply need to know that when we call the method, we will achieve a desired outcome. In our example, we don’t need to know anything about the on() method apart from the fact that using it on our LED object will make the physical LED light up.

--- /collapse ---

_Image by Rosapicci (Own work) [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons_

### What you will learn

This project covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum){:target="_blank"}:

+ [Apply higher-order programming techniques to solve real-world problems](https://curriculum.raspberrypi.org/programming/maker/){:target="_blank"}

### Additional information for educators

If you need to print this project, please use the [printer-friendly version](https://projects.raspberrypi.org/en/projects/deck-of-cards/print){:target="_blank"}.

Use the link in the footer to access the GitHub repository for this project, which contains all resources (including an example finished project) in the 'en/resources' folder.
