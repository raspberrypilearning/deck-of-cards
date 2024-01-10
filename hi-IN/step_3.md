## एक क्लास(class) बनाएँ

एक **क्लास(class)** ऑब्जेक्ट(object) को बनाने के लिए एक टेम्पलेट(template) की तरह है। कुकी कटर के समान एक क्लास(class) के बारे में सोचें - यह आपके द्वारा बनाये गये सभी कुकी ऑब्जेक्ट्स(objects) के लिए एक टेम्पलेट(template) है। आप कुकी ऑब्जेक्ट्स(objects) के जितने चाहें उतने उदाहरण(instances) बना सकते हैं, और वे सभी एक ही टेम्पलेट(template) से शुरू होंगे। 

<video width="768" height="576" controls>
<source src="resources/Cementyourknowledgeofobjects_sd.mp4" type="video/mp4">
आपका ब्राउज़र वीडियो का समर्थन नहीं करता है, FireFox या Chrome आज़माएँ|
</video>

जब आप असली कुकीज़ बनाते हैं, तो आप उन्हें एक ही कुकी कटर से बनाते हैं, लेकिन आप प्रत्येक व्यक्तिगत कुकी को अनुकूलित कर सकते हैं, उदाहरण के लिए कुछ आइसिंग या कुछ स्प्रिंकल मिला कर। यह एक क्लास(class) का उपयोग करके बनाये गये ऑब्जेक्ट्स(objects) के साथ समान है - आप इसमें अलग-अलग डेटा संग्रहीत करके प्रत्येक ऑब्जेक्ट(object) को अनु कूलित कर सकते हैं आइए देखें कि यह अभ्यास में कैसे काम करता है।

### एक क्लास(class) बनाये

आप `Card` क्लास(class) बनाकर शुरू करने जा रहे हैं जो ताश का ऑब्जेक्ट(objects) बनाने के लिए एक टेम्पलेट(template) के रूप में कार्य करेगा।

प्रत्येक कार्ड ऑब्जेक्ट(object) **Card** क्लास(class) का एक अलग `उदाहरण(instance)` है । उदाहरण के लिए, हो सकता है कि आपके पास हुकुम की पंजी का प्रतिनिधित्व(represent) करने वाला कार्ड ऑब्जेक्ट(object) हो और पान की दुक्की का प्रतिनिधित्व करने वाला कोई अन्य कार्ड ऑब्जेक्ट(object) हो।

हमारे ताश के पत्ते को नीचे दिए गए चित्रों की बजाय पाठ के रूप में दर्शाया जाएगा।

![5 का हुकुम](images/five-of-spades.png)

आप चुन सकते हैं कि वीडियो देखना है या लिखित निर्देशों का उपयोग करना है।

<video width="768" height="576" controls>
<source src="resources/clip1.mp4" type="video/mp4">
आपका ब्राउज़र वीडियो का समर्थन नहीं करता है, FireFox या Chrome आज़माएँ|
</video>

+ एक नयी Python फ़ाइल खोलें और इसे `card.py` के रूप में जमा करें ।

+ `Card` क्लास(class) बनाकर प्रारंभ करें:

```python
class Card:
```

क्लास(class) के नाम आमतौर पर एक बड़े अक्षर के साथ लिखे जाते हैं ताकि वे वेरियबल(variable) नामों से आसानी से अलग हो सकें।

इसके बाद, आप क्लास(class) में एक **विधि(method)** जोड़ने जा रहे हैं। विधियाँ(methods) फंक्शन(function) के बहुत समान हैं, और हम ऑब्जेक्ट(objects) के साथ परस्पर प्रभाव डालने के लिए उनका उपयोग करते हैं।

### विधियां(methods)

Python कोड लिखते समय आपको पहले से ही फंक्शन(function) का सामना करना पड़ सकता है। फंक्शन(functions) हमें निर्देशों के एक सेट को एक नाम देने की अनुमति देते हैं। आप किसी फ़ंक्शन(function) को पैरामीटर(parameter) के रूप में डेटा पास(pass) कर सकते हैं, और वैकल्पिक रूप से आपके पास इसके परिणामस्वरूप कुछ डेटा वापस(return) कर सकते हैं।

किसी फ़ंक्शन(function) और विधि(method) के बीच का अंतर यह है कि विधि(method) को **किसी ऑब्जेक्ट(object) पर** कहा(call) जाता है । इसका मतलब यह है कि एक विधि(method) ऑब्जेक्ट(object) के अंदर संग्रहीत सभी डेटा का उपयोग कर सकती है, साथ ही किसी भी डेटा को जो आप इसे पैरामीटर(parameter) के रूप में पास(pass) करते हैं।

### एक `__init__` विधि(method) बनाएं|

Python में, हर क्लास की एक विशेष विधि(method) होती है जिसे `__init__` कहा जाता है जो बताता है कि कैसे बनाएँ (या **इनिशियलाइज़(initialize)**  करें) एक ऑब्जेक्ट(object) को। इस विशेष विधि(method) का नाम हमेशा `init`के दोनों ओर एक दोहरा अंडरस्कोर('_') होता है ।

+ एक `__init__` विधि(method) अपने `Card` क्लास(class) के अंदर बनाएं:

```python
class Card:
    def __init__(self):
```

--- collapse ---
---
title: मुझे `self` की आवश्यकता कोष्ठक('()') में क्यों है?
---

कार्य करने के लिए एक विधि(method) को संदर्भ की आवश्यकता होती है। `self` ऑब्जेक्ट(object) का संदर्भ है, और इसे किसी भी `क्लास(class)` विधि(method) में पारित होने वाला पहला पैरामीटर(parameter) होना चाहिए। ऐसा इसलिए है क्योंकि इस विधि(method) को यह जानने की आवश्यकता है कि इसे क्या बुलाया(called) जा रहा है, ताकि यह ऑब्जेक्ट के भीतर संग्रहीत डेटा का उपयोग कर सके।

आइए एक उदाहरण देखें:

OOP के बाहर, एक ही वेरिएबल(variable) साझा करने के लिए दो फंक्शन(function) के लिए, यह वैश्विक(global variable) होना चाहिए:

```python
name = "Laura"

def hi():
    print("Hi " + name)

def bye():
    print("Bye " + name)
```

एक क्लास(class) के अंदर, `self` वेरिएबल(variable) साझा करने के लिए इस्तेमाल किया जा सकता है।

```python
class Welcome():
    def __init__(self):
        self.name = "Laura"

    def hi(self):
        print("Hi " + self.name)

    def bye(self):
        print("Bye " + self.name)
```

यहाँ, हमने वैरिएबल(variable) को परिभाषित किया `self.name` और इसका मान(value) `"Laura"` पर सेट करें `__init__` विधि(method) के अंदर जो इस क्लास(class) के ऑब्जेक्ट(object) को इनिशियलाइज़(initialize) करती है। इस प्रकार सभी ऑब्जेक्ट्स(objects) में एक वेरियबल(variable) `self.name` `"Laura"` पर सेट होगा । `hi()` और `bye()` हम जिन विधियाँ(methods) को परिभाषित करते हैं, वे अब `self.name` में संग्रहीत जानकारी का उपयोग कर सकते हैं ।

--- /collapse ---

### विशेषताएँ(attributes)

विशेषताएँ(attributes) किसी ऑब्जेक्ट(object) के अंदर संग्रहीत जानकारी के टुकड़े हैं, न कि उस ऑब्जेक्ट(object) से जुड़े वेरिएबल(variable) के संग्रह की तरह। कार्ड ऑब्जेक्ट दो विशेषताओं(attributes) के साथ शुरू होगा, `suit` और `number`, और हम उन्हें `self` के साथ उपसर्ग करेंगे यह दिखाने के लिए कि वे ऑब्जेक्ट(object) उदाहरण(instance) के हैं।

+ दो विशेषताओं(attributes) को अपने `__init__` विधि(method) और दो पैरामीटर जोड़े, ताकि आप ऑब्जेक्ट बनाते समय उनके मानों को आर्ग्यूमेंट्स(arguments) के रूप में पारित कर सकें:

```python
def __init__(self, suit, number):
    self.suit = suit
    self.number = number
```