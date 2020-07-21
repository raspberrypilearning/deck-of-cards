## ताश के पत्तों की गड्डी(डेक)

अब जब आपके पास कार्ड का एक बुनियादी मॉडल है, तो यह एक डेक बनाने का समय है।

+ एक `Deck` क्लास बनाएँ । आप इसे उसी फ़ाइल में कर सकते हैं जहाँ आपने अपना `Card` क्लास(class) लिखा थी, या एक अलग से। यदि आप इसे एक अलग फ़ाइल में करते हैं (उदाहरण `deck.py`), आपको इस कोड के साथ उस फ़ाइल के शुरू में `Card`क्लास(class) आयात करनी होगी:

```python
from card import Card
```

कोड की इस पंक्ति में, `card` Python फ़ाइल का नाम जिसमें क्लास(class) है, जो `.py` विस्तार के बिना है, और `Card` क्लास(class) का नाम है।

+ एक नयी`Deck` क्लास(class) और एक `__init__` विधि(method) इसमें बनाएँ। इस बार हमें `self` के अलावा किसी भी पैरामीटर(parameter) की जरुरत नहीं होगी, जो अनिवार्य है।

```python
class Deck:

    def __init__(self):
```

+ `Deck` को कार्ड की एक सूची संग्रहीत करने की आवश्यकता होगी, जिनमें से प्रत्येक `Card` ऑब्जेक्ट(object) होगा । `__init__` विधि(method) में `_cards` नामक एक विशेषता(attribute) जोड़ें, और इसे अभी के लिए एक खाली सूची के रूप में परिभाषित करें।

```python
class Deck:

    def __init__(self):
        self._cards = []
```

+ अब 52 आवश्यक कार्ड के साथ गड्डी को बनाने के लिए एक विधि(method) लिखते हैं। `populate` नामक एक विधि(method) बनाकर शुरू करें:

```Python
def populate(self):
```

+ अपनी विधि(method) के अंदर, दो सूचियों को परिभाषित करें। एक में सभी संभावित कार्ड सूट होने चाहिए, और अन्य में सभी संभव कार्ड नंबर शामिल होना चाहिए:

```Python
def populate(self):
    suits = ["hearts", "clubs", "diamonds", "spades"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
```

--- collapse ---
---
title: क्या संख्याओं की सूची बनाने का एक अधिक कुशल तरीका है?
---

हाँ! उन सभी को लिखने के बजाय, आप **सूची समझ** का उपयोग कर सकते हैं, जो मौजूदा सूची के आधार पर एक नई सूची बनाने का एक तेज़ तरीका है।

इसलिए, स्ट्रिंग्स(strings) के रूप में 2 से 10 की संख्या वाली एक सूची बनाने के लिए, आप कोड का उपयोग कर सकते हैं:

```Python
numbers = [str(n) for n in range(2,11)]
```

इसका मतलब है की:
- मुझे `str(n)` (n का स्ट्रिंग संस्करण(string version)) दे दो
- प्रत्येक `n के लिए रेंज(range) में (2, 11)` (याद रखें कि `range())` फंक्शन(function) 2 से शुरू होगा और (11 शामिल नहीं है) 11 पर रुकेगा

फिर चित्र सूची और अंत में इक्का युक्त सूची जोड़ें:

```Python
numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
```

--- /collapse ---

+ ताकि `populate` कार्ड के डेक को उत्पन्न करता है, हमें बस दो सूचियों से वस्तु को संयोजित करना है - प्रत्येक सूट के लिए, प्रत्येक संख्या के लिए, एक `कार्ड` ऑब्जेक्ट(object) बनाएं । ऐसा करने का एक तरीका नेस्टेड लूप(nested loops) के साथ है:

```Python
cards = []                          # कार्डों की एक खाली सूची बनाएं
for suit in suits:                  # प्रत्येक सूट के लिए...
    for number in numbers:          # प्रत्येक नंबर के लिए...
        # एक नया कार्ड ऑब्जेक्ट बनाएं और इसे सूची में जोड़ें
        cards.append( Card(suit, number) )  
self._cards = cards                 # फिर इस सूची में self._cards इंगित करें
```

हालाँकि, नेस्टेड लूप(nested loops) का उपयोग करने से आपका कोड अधिक जटिल हो सकता है। कोड को सरल बनाने के लिए, आप **सूची की समझ** उपयोग कर सकते हैं:

```Python
self._cards = [ Card(s, n) for s in suits for n in numbers ]
```

इस कोड का मतलब है:
- सेट करें `self._cards` को
- `[ एक सूचि ] में`
- `कार्ड` ऑब्जेक्ट्स(objects) के
- `s, n` के हर संयोजन से युक्त, लूपिंग(looping) `for s in suits` और `for n in numbers` के माध्यम से

यदि आप सूची की समझ के बारे में अधिक जानना चाहते हैं, तो नीचे दी गई जानकारी पर एक नज़र डालें।

[[[generic-python-simple-list-comprehensions]]]

+ चलो परीक्षण करते हैं कि क्या आपकी विधि(method) ठीक से एक डेक का निर्माण करती है। अपने `__init__` विधि में वापस जाएं, `populate()` विधि(method) को बुलाये, फिर कार्ड की सूची का प्रिंट आउट(print-out) लें:

```Python
def __init__(self):
    self._cards = []
    self.populate()
    print(self._cards)
```

+ `Deck` क्लास(class) का एक उदाहरण(instance) बनाएँ यह जाँचने के लिए कि क्या आपको वह डेक मिल रहा है जो आप चाहते हैं।

--- hints ---


--- hint ---

एक वेरिएबल(variable declare) घोषित करके और इसे `Class()` के बराबर बनाकर एक क्लास(class) का एक उदाहरण(instance) बनाएं ।

--- /hint ---

--- hint ---

समीक्षा करें कि आपने `Card` क्लास(class) का एक ऑब्जेक्ट(object) को कैसे बनाया है।

--- /hint ---

--- hint ---

इस कोड का उपयोग करें:

```Python
my_deck = Deck()
```

--- /hint ---

--- /hints ---

आपको निम्न आउटपुट(output) दिखना चाहिए:

```Python
[2 of hearts, 3 of hearts, 4 of hearts, 5 of hearts, 6 of hearts, 7 of hearts, 8 of hearts, 9 of hearts, 10 of hearts, J of hearts, Q of hearts, K of hearts, A of hearts, 2 of clubs, 3 of clubs, 4 of clubs, 5 of clubs, 6 of clubs, 7 of clubs, 8 of clubs, 9 of clubs, 10 of clubs, J of clubs, Q of clubs, K of clubs, A of clubs, 2 of diamonds, 3 of diamonds, 4 of diamonds, 5 of diamonds, 6 of diamonds, 7 of diamonds, 8 of diamonds, 9 of diamonds, 10 of diamonds, J of diamonds, Q of diamonds, K of diamonds, A of diamonds, 2 of spades, 3 of spades, 4 of spades, 5 of spades, 6 of spades, 7 of spades, 8 of spades, 9 of spades, 10 of spades, J of spades, Q of spades, K of spades, A of spades]
```
